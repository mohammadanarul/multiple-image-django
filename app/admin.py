from django.contrib import admin
from .models import Order, Image

admin.site.register([Order, Image])
