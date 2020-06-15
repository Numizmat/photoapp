from django.shortcuts import render
from django.views.generic import ListView
from django.template.response import TemplateResponse
from .models import Image, Thumbnail, Image2


def gallery(request):
    image_all = Image.objects.all()
    image_gal = {'image_all': image_all}

    image2_all = Image2.objects.all()
    image2_gal = {'image2_all': image2_all}

    thumb_all = Thumbnail.objects.all()
    gallery = {'thumb_gal': thumb_all, 'image_gal': image_all, 'image2_gal': image2_all}

    return render(request, 'galleryapp/gallery.html', gallery)


class ItemList(ListView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        context['settings'] = Image.objects.all()
        return context
