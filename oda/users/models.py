from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    profile_image = models.ImageField(
        "profile image", upload_to="users/profile", blank=True
    )
    profile_thumbnail = ImageSpecField(source='profile_image',
                                      processors=[ResizeToFill(20, 20)],
                                      format='JPEG',
                                      options={'quality': 60})
    profile_thumbnail2 = ImageSpecField(source='profile_image',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 60})
    def __str__(self):
        return self.username
    