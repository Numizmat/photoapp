from django.contrib import admin
from .models import SaveImg

admin.site.register(SaveImg)


# class SaveImgInline(admin.TabularInline):
#     model = SaveImg
#
#
# class ImgAdmin(admin.ModelAdmin):
#     inlines = [
#         SaveImgInline,
#     ]
