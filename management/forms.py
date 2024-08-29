from .models import Product, ScannedProducts, CashierDynamicProducts, ProductType, UserCreationValidation,\
    Expenses
from django.forms import Select, DateInput, Textarea, TextInput, ModelForm, SelectMultiple, NumberInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class AddExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense', 'description', 'image']
        widgets = {
            'expense': NumberInput(attrs={
                'class': "add-expense-field",
            }),
            'description': Textarea(attrs={
                'class': 'add-expense-field auto-growth',
                'placeholder': 'Expense Description',
            }),
        }


class ExpenseDetailsEditForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense', 'description', 'image']
        widgets = {
            'expense': NumberInput(attrs={
                'class': "expense-data-field",
                'placeholder': 'Product Name'
            }),
            'description': Textarea(attrs={
                'class': "expense-data-field auto-growth",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make all fields not required
        for field_name, field in self.fields.items():
            field.required = False


class RegistrationValidationForm(ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'registration_validation_field',
                                          'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'registration_validation_field',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
    )

    class Meta:
        model = UserCreationValidation
        fields = [
            'username', 'email', 'group'
        ]
        widgets = {
            'username': TextInput(attrs={
                'class': "registration_validation_field",
                'placeholder': 'Username'
            }),
            'email': TextInput(attrs={
                'class': "registration_validation_field",
                'placeholder': 'Email Address'
            }),
            'group': Select(attrs={
                # 'class': "registration_validation_select_field",
                'class': "registration_validation_field",
            }),
        }


class ProductTypeForm(ModelForm):
    class Meta:
        model = ProductType
        fields = ['product_type', 'image']
        widgets = {
            'product_type': TextInput(attrs={
                'class': "add-product-type-field",
            })
        }


class ScannedProductSubtractQuantityForm(ModelForm):
    class Meta:
        model = CashierDynamicProducts
        fields = ['scanned_quantity']
        widgets = {
            'scanned_quantity': TextInput(attrs={
                'class': "scanned-quantity-field",
            })
        }


class ScannedProductAddQuantityForm(ModelForm):
    class Meta:
        model = CashierDynamicProducts
        fields = ['scanned_quantity']
        widgets = {
            'scanned_quantity': TextInput(attrs={
                'class': "scanned-quantity-field",
            })
        }


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'register-field',
               'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'register-field',
               'placeholder': 'Confirm Password'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists!")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': "register-field",
                'placeholder': 'Username'
            }),
            'email': TextInput(attrs={
                'class': "register-field",
                'placeholder': 'Email'
            }),
        }


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = ProductType.objects.filter(removed=False)

    class Meta:
        model = Product
        fields = ['name', 'type', 'barcode', 'price', 'expiry_date', 'quantity', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': "product-inventory-field",
                'placeholder': 'Product Name'
            }),
            'expiry_date': DateInput(attrs={
                'class': "product-inventory-field",
                'type': 'date',
            }),
            'barcode': TextInput(attrs={
                'class': "product-inventory-field",
                'placeholder': 'Barcode'
            }),
            'price': NumberInput(attrs={
                'class': "product-inventory-field",
                'placeholder': 'Product Price'
            }),
            'quantity': NumberInput(attrs={
                'class': "product-inventory-field",
                'placeholder': 'Stock'
            }),
            'type': Select(attrs={
                'class': "product-inventory-field",
            }),
        }


class ChangeProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'type', 'barcode', 'price', 'expiry_date', 'quantity', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': "product-profile-field",
                'placeholder': 'Product Name'
            }),
            'expiry_date': DateInput(attrs={
                'class': "product-profile-field",
                'type': 'date',
            }),
            'barcode': TextInput(attrs={
                'class': "product-profile-field",
                'placeholder': 'Barcode'
            }),
            'price': NumberInput(attrs={
                'class': "product-profile-field",
                'placeholder': 'Product Price'
            }),
            'quantity': NumberInput(attrs={
                'class': "product-profile-field",
                'placeholder': 'Stock'
            }),
            'type': Select(attrs={
                'class': "product-profile-field",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make all fields not required
        for field_name, field in self.fields.items():
            field.required = False


class ScanningProductTestForm(ModelForm):

    class Meta:
        model = ScannedProducts
        fields = ['product']
        widgets = {
            'product': SelectMultiple(attrs={
                'class': "product-catalogue-field",
            }),
        }

    def __init__(self, user, *args, **kwargs):
        super(ScanningProductTestForm, self).__init__(*args, **kwargs)
        # Filter the products based on the logged-in user
        self.fields['product'].queryset = CashierDynamicProducts.objects.filter(cashier=user)
