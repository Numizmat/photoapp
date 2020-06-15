from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=150, blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    data_pub = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos')
    exif_data = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Thumbnail(models.Model):
    # key =models.ForeignKey(Image, on_delete = models.CASCADE)
    title = models.CharField(max_length=20, null=True)
    thumb = models.ImageField(upload_to='thumbnail')
    date_pub = models.DateTimeField()

    def __str__(self):
        return self.title


class Image2(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    data_pub = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos2')
    exif_data = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
