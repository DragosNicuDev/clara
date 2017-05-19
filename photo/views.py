from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import PhotoUploadForm
from .models import PhotoUpload


class PhotoUploadCreate(SuccessMessageMixin, CreateView):
    model = PhotoUpload
    template_name = 'upload_photo.html'
    form_class = PhotoUploadForm

    def get_success_url(self):
        return reverse('upload:upload-photo')
    success_message = 'Congratulations! Your photo has been uploaded and is now under review.'
