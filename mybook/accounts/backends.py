from django.contrib.auth.backends import ModelBackend
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrMobileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(models.Q(email=username) | models.Q(mobile_number=username))
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
