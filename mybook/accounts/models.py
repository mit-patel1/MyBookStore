from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username
