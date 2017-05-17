from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Admin option to select from
PHOTO_STATUS = (
    ('ir', 'In Review'),
    ('ap', 'Approved'),
    ('de', 'Deleted'),
)


# Main photo upload app
class PhotoUpload(models.Model):
    '''After the user finishes the challenge
    he can upload a photo using this app'''
    # The date when a user uploads a photo
    date_upload = models.DateTimeField(default=timezone.now)
    # The status of the photo
    status = models.CharField(max_length=2, default='ir', choices=PHOTO_STATUS)
    # The date when the admin aproves the photo
    date_approved = models.DateTimeField(auto_now=True,
                                         blank=True,
                                         null=True)

    def path_and_rename(instance, filename):
        extension = filename.split('.')[-1]
        user = User.objects.get(username='EuSuntDan')
        if User.is_authenticated:
            return 'uploads/{}-{}.{}'.format(user,
                                             instance.date_upload,
                                             extension)
        else:
            return 'uploads/{}.{}'.format(instance.date_upload, extension)

    image = models.ImageField(upload_to=path_and_rename,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.status
