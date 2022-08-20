from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views import HomeView, download_images_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('order/images/downlad/<pk>/', download_images_view, name='order-images-downliad'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)