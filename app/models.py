from django.db import models

class Order(models.Model):
    title = models.CharField(max_length=255)


class Image(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='order-images/', max_length=10485760)



class ImageStore(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.FileField(upload_to='image-store/', max_length=524288)
