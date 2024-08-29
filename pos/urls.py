"""pos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views
from pos import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('login/', views.authentication, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('scanned-products/<str:username>/', views.scanning_products, name='scanned-products'),
    path('scanned-products/cashier/<str:username>/', views.scanning_products_cashier, name='scanned-products-cashier'),
    path('function/sell-products/<str:username>/', views.sell_scanned_products, name='sell-scanned-products'),
    path('function/add-dynamic-products/<str:username>/', views.add_dynamic_products, name='add-product-cashier'),
    # path('scan/<str:username>/', views.scan_barcodes, name='scanning'),
    path('remove-scanned-product/<str:username>/<str:barcode>/', views.remove_scanned_product, name='remove-product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('products/expired/', views.expired_products, name='expiration'),
    path('products/sold-out/', views.sold_out_products, name='sold-out-products'),
    path('products/sold/', views.products_sold, name='sold-products'),
    path('products/select/<str:username>/', views.select_products_sell, name='select-sell'),
    path('products/select/cashier/<str:username>/', views.select_products_sell_cashier_group,
         name='select-sell-cashier'),
    path('test/<str:username>', views.update_scanned_products, name='test-update'),
    path('expired_products/', views.expired_products_json, name='expired-products-json'),
    path('delete-notification/<str:title>/<int:id>/', views.remove_notification, name='delete-notification'),
    path('seen-notifications/', views.seen_notifications, name='seen-notifications'),
    path('product/<int:id>/', views.product_info, name='product-info'),
    path('products/', views.products_all, name='products'),
    path('refund-product/<int:sold_product_id>/<int:sold_products_id>/', views.refunded_product, name='refund-product'),
    path('refund/<int:sold_products_id>/', views.refund, name='refund'),
    path('receipt-search/', views.refund_search, name='refund-search'),
    path('htmx/clear-change/<str:username>/', views.clear_scanned_header_change, name='htmx-clear-change'),
    path('add-quantity-htmx/<str:username>/<str:barcode>/', views.add_quantity_product,
         name='add-quantity'),
    path('subtract-quantity-htmx/<str:username>/<str:barcode>/', views.subtract_quantity_product,
         name='subtract-quantity'),
    path('registration/', views.registration_validation, name='registration-validation'),
    path('registrants-validation/', views.validation_registrants, name='registrant-validation'),
    path('confirm_registration/<str:username>/', views.confirm_registration, name='confirm-registration'),
    path('deny-registration/<int:id>/', views.deny_registration, name='deny-registration'),
    path('download-income/', views.download_income_excel, name='income-excel'),
    path('download-expenses/', views.download_expense_excel, name='expenses-excel'),
    path('download-revenues/', views.download_revenue_excel, name='revenue-spreadsheet'),
    path('download-revenues-filtered/', views.download_revenue_excel_filtered, name='revenue-spreadsheet-filtered'),
    path('download-income-filtered/', views.download_income_excel_filtered, name='income-spreadsheet-filtered'),
    path('download-expenses-filtered/', views.download_expense_excel_filtered, name='expense-spreadsheet-filtered'),
    path('report/expenses/', views.expenses_page, name='expenses'),
    path('report/income/', views.income_page, name='income'),
    path('report/revenue/', views.revenue_page, name='revenues'),
    path('expense/detail/<int:id>/<str:expense_date>/', views.modify_expense_details, name='expense-details'),
    path('add/expense/', views.add_expense, name='add-expense'),
    path('async-search/<str:username>/', views.async_product_search, name='async-search'),
    path('product-types/', views.product_types, name='product-types'),
    path('remove/product_type/<str:name>/<int:id>/', views.remove_product_type, name='remove-product-type'),
    path('expiry-date-conf/', views.expiry_date_conf_page, name='expiry-date-conf'),
    path('resubscribe/', views.resubscribe, name='resubscribe')
    # path('htmx/sell/<str:username>/', views.tester, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()