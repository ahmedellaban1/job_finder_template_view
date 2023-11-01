from django.contrib.auth.models import AbstractUser
from django.db import models
from etc.choices import USER_TYPE
from etc.file_uploader import user_image


class CustomUser(AbstractUser):
    type = models.CharField(max_length=10, choices=USER_TYPE, default=USER_TYPE[1][1])
    image = models.ImageField(upload_to=user_image, null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username
