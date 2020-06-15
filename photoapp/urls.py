from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from photoapp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('upload/', include('uploadapp.urls')),
    path('gallery/', include('galleryapp.urls')),
    path('album/', include('albumapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)