from django.shortcuts import render
from django.views.generic import ListView
from galleryapp.models import Image, Thumbnail
from .forms import AlbumForm


def album(request):
    image_all = Image.objects.all()
    image_gal = {'image_all': image_all}

    thumb_all = Thumbnail.objects.all()
    gallery = {'thumb_gal': thumb_all, 'image_gal': image_all}

    return render(request, 'albumapp/album.html', gallery)


def album_upload_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
    else:
        form = AlbumForm()
    return render(request, 'albumapp/album.html', {'form': form})