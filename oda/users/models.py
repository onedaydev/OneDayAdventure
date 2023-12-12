from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(
        "profile image", upload_to="users/profile", blank=True
    )

    def __str__(self):
        return self.username