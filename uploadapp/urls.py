from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.image_upload_view, name='upload')
]
