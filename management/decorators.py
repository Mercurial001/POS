from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from .models import DeviceInformation
from django.contrib.auth.models import User
from functools import wraps
from django.utils import timezone
import os
import subprocess
from django.shortcuts import render, redirect
import getpass


def superuser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            rendered_template = render(request, 'forbidden_template.html', {'variable': 'value'})
            return HttpResponseForbidden(rendered_template)
    return wrapper_func


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif group == 'admin':
                return view_func(request, *args, **kwargs)
            elif group == 'cashier':
                return redirect('scanned-products-cashier', username=request.user.username)
            else:
                return HttpResponseForbidden("You don't have permission to access this page.")
        return wrapper_func
    return decorator


# def has_expired(view_func):
#     @wraps(view_func)  # Keeps the original function's metadata intact
#     def wrapper_func(request, *args, **kwargs):
#         device_user = os.getlogin()
#
#         # Determine the appropriate command based on the OS
#         command = ''
#         if os.name == 'nt':  # Windows
#             command = 'wmic bios get serialnumber'
#         elif os.name == 'posix':  # Unix-based systems
#             if 'darwin' in os.sys.platform:  # MacOS
#                 command = "system_profiler SPHardwareDataType | grep 'Serial Number'"
#             else:  # Linux
#                 command = 'cat /sys/class/dmi/id/product_serial'
#
#         # Execute the command and retrieve the serial number
#         serial_number = subprocess.check_output(command, shell=True).decode().strip()
#         serial_number_lines = serial_number.splitlines()
#
#         # Take the last line which should be the actual serial number
#         serial_number = serial_number_lines[-1].strip()
#
#         # Get or create the device record
#         device, created = DeviceInformation.objects.get_or_create(
#             name=f'{device_user}-{serial_number}',
#             defaults={'registration_date': timezone.now().date()}
#         )
#
#         # If the device doesn't have an expiry date, redirect to set it
#         if device.expiry_date is None:
#             return redirect('expiry-date-conf')
#
#         # If the device has expired, redirect to resubscribe
#         if device.expiry_date < timezone.now().date():
#             return redirect('resubscribe')
#
#         # Otherwise, proceed with the original view
#         return view_func(request, *args, **kwargs)
#
#     return wrapper_func
def has_expired(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        try:
            device_user = os.getlogin()
        except OSError:
            device_user = getpass.getuser()

        serial_number = None

        if os.name == 'nt':  # Windows
            command = 'wmic bios get serialnumber'
        elif os.name == 'posix':  # Unix-based systems
            if 'darwin' in os.sys.platform:  # MacOS
                command = "system_profiler SPHardwareDataType | grep 'Serial Number'"
            else:  # Linux
                command = 'cat /sys/class/dmi/id/product_serial 2>/dev/null'

            try:
                serial_number = subprocess.check_output(command, shell=True).decode().strip()
                serial_number_lines = serial_number.splitlines()
                serial_number = serial_number_lines[-1].strip()
            except subprocess.CalledProcessError:
                # Handle the error, maybe log it or set a default/fallback serial number
                serial_number = "UNKNOWN_SERIAL"

        if serial_number is None:
            serial_number = "UNKNOWN_SERIAL"

        device, created = DeviceInformation.objects.get_or_create(
            name=f'{device_user}-{serial_number}',
            defaults={'registration_date': timezone.now().date()}
        )

        if device.expiry_date is None:
            return redirect('expiry-date-conf')

        if device.expiry_date < timezone.now().date():
            return redirect('resubscribe')

        return view_func(request, *args, **kwargs)

    return wrapper_func


def admin_group_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated and is a member of the 'admin' group
        if request.user.is_authenticated and request.user.groups.filter(name='admin').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")

    return _wrapped_view
