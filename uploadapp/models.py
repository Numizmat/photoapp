from django.db import models
from galleryapp.models import Image


class Save(models.Model):
    user = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='saved')
    text = models.TextField(blank=False, max_length=500)


class SaveImg(models.Model):
    image = models.ImageField(upload_to='saved')
    save = models.ForeignKey(Save, on_delete=models.CASCADE, related_name='images')
