from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('analytics',include('apps.analytics.urls')),
    path('cart',include('apps.cart.urls')),
    path('catalog',include('apps.catalog.urls')),
    path('orders',include('apps.orders.urls')),
    path('payments',include('apps.payments.urls')),
    path('reviews',include('apps.reviews.urls')),
    path('users',include('apps.users.urls')),
    path('',include('apps.navigation.urls')),
]