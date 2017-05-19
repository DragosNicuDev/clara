from django.conf.urls import url
from photo.views import PhotoUploadCreate


urlpatterns = [
    url(r'^upload/$', PhotoUploadCreate.as_view(), name='upload-photo'),
]
