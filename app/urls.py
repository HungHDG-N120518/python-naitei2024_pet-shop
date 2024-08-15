from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path(
        '',
        views.index,
        name='index'),
    path(
        'shop/',
        views.ShopView,
        name='shop'),
    path(
        'sign-in/',
        views.login_view,
        name="sign-in"),
    path(
        'sign-up/',
        views.signup_view,
        name="sign-up"),
    path(
        '',
        include('django.contrib.auth.urls')),
    path(
        'product/<int:id>/',
        views.product_detail_view,
        name='product_detail'),
    path(
        'get-price/',
        get_price,
        name='get_price'),
    path(
        'get-available-options/',
        get_available_options,
        name='get_available_options'),
    path(
        'get-product-detail-id/',
        get_product_detail_id,
        name='get_product_detail_id'),
    path(
        'add-to-cart/',
        add_to_cart,
        name='add_to_cart'),
    path(
        'verify-input/',
        views.verify_input,
        name="verify-input"),

    path(
        'search-products/',
        views.search_products,
        name='search_products'),
    path(
        'vouchers/',
        voucher_list,
        name='voucher_list'),
]
