from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import ObjectGallery, ObjectGalleryImage


def index(request):
    return render(request, 'mainapp/index.html')


def object_gallery(request, gallery_id):
    gallery_images = ObjectGalleryImage.objects.filter(gallery=gallery_id).values('image', )
    gallery_images = list(gallery_images)
    return JsonResponse(gallery_images,safe=False)