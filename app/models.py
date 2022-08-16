from django.db import models

class Order(models.Model):
    title = models.CharField(max_length=255)


class Image(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='images')
    images = models.FileField()
