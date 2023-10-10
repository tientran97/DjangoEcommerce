
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from Irvin.settings import MEDIA_ROOT

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
