from django.contrib import admin
from django.urls import path, include
from . import views
from .views import object_gallery


urlpatterns = [
    path('', views.index, name='index'),
    path('object_gallery/<int:gallery_id>/', object_gallery, name = 'object_gallery')
]
