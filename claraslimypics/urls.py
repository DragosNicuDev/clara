"""claraslimypics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from carousel.views import CarouselView
from photos.views import PhotoUploadCreate

admin.site.site_header = "Clara's Slimy Pics"
admin.site.site_title = "Clara's Slimy Pics"

urlpatterns = [
    url(r'^$', CarouselView.as_view(), name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$',
        PhotoUploadCreate.as_view(), name='upload-photo'),
    url(r'^success/$',
        TemplateView.as_view(template_name="success.html"), name='success')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
