from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.conf import settings
from .models import Order, Image
from zipfile import ZipFile
from wsgiref.util import FileWrapper


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orders'] = Order.objects.all()
        return context

    
    def post(self, *args, **kwargs):
        title = self.request.POST['title']
        images = self.request.FILES.getlist('images')
        order_ = Order.objects.create(title=title)
        for image in images:
            Image.objects.create(order=order_, images=image)
        return redirect('/')


def download_images_view(request, pk):
    order_image = Order.objects.get(pk=pk)
    # get a qs of assigned illustrations
    all_images = order_image.images.all()
    
    with ZipFile(f'{order_image.title}.zip', 'w') as export_zip:
        for order_img in all_images:
            img_path =  order_img.images.path
            # below line should result in .write("/media/somefolder/image123.png", image123.png)
            export_zip.write(img_path, img_path.split("/")[-1])

    wrapper = FileWrapper(open('export.zip', 'rb'))
    content_type = 'application/zip'
    content_disposition = f'attachment; filename={order_image.title}.zip'

    response = HttpResponse(wrapper, content_type=content_type)
    print('respose', response)
    response['Content-Disposition'] = content_disposition
    return response

'''
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orders'] = Order.objects.all()
        return context

    
    def post(self, *args, **kwargs):
        title = self.request.POST['title']
        images = self.request.FILES.getlist('images')
        order_ = Order.objects.create(title=title)
        for image in images:
            Image.objects.create(order=order_, images=image)
        return redirect('/')
'''