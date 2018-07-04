from django.core.validators import RegexValidator
from django.db import models

USERNAME_LENGTH = 10
PASSWORD_LENGTH = 20


class User(models.Model):
    _username = models.CharField(primary_key=True, max_length=USERNAME_LENGTH, unique=True)
    _password = models.CharField(max_length=PASSWORD_LENGTH)
    _is_manager = models.BooleanField(default=False)
    _name = models.CharField(max_length=100)

    def get_id(self):
        return self._username

    def get_name(self):
        return self._name

    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.objects.get(username=username, password=password)
        except cls.DoesNotExist:
            return None
