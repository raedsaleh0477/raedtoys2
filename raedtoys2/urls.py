"""
URL configuration for raedtoys2 project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Project Apps URLs
    path('accounts/', include('accounts.urls')),   # حسابات المستخدمين
    path('', include('catalog.urls')),              # الصفحة الرئيسية + الألعاب
    path('orders/', include('orders.urls')),        # السلة والطلبات
]

# Media files (development only)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
