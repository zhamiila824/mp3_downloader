from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import settings
from download import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

