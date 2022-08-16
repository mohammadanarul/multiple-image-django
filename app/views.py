from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.conf import settings
from .models import Order, Image
from zipfile import ZipFile


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

    order_image_url = []
    for image in order_image.images.all():
        image_path = settings.MEDIA_ROOT+ image.images.url
        order_image_url.append(image_path)
    
    image_name = 'whatevername.png';

    # print(order_image_url)
    # return redirect('/')

    with ZipFile('export.zip', 'w') as export_zip:
        export_zip.write(order_image_url, image_name)

    wrapper = FileWrapper(open('export.zip', 'rb'))
    content_type = 'application/zip'
    content_disposition = 'attachment; filename=export.zip'

    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Disposition'] = content_disposition
    print(content_disposition)
    return response
