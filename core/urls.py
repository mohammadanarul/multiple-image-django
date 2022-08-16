from django.contrib import admin
from django.urls import path
from app.views import HomeView, download_images_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('order/images/downlad/<pk>/', download_images_view, name='order-images-downliad'),
]
