from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from galleryapp.models import Image


class Index(models.Model):
    title = models.CharField(max_length=30)


class ObjectGallery(models.Model):
    object = models.ForeignKey(Image, verbose_name='Объект', on_delete=models.CASCADE)
    name = models.CharField('Загаловок галереи', max_length=255)
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея ообъекто'
        verbose_name_plural = 'Объекты(загруженные фотографии)'


def image_upload_path(instance, filename):
    object_crm_id = instance.gallery.object.crm_id


class ObjectGalleryImage(models.Model):
    gallery = models.ForeignKey(ObjectGallery, verbose_name='Галерея', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='object')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(128, 128)],
                                     options={'quality': 70}
                                     )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


