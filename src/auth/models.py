from django.db import models

USERNAME_LENGTH = 10
PASSWORD_LENGTH = 20

class User(models.Model):
    _username = models.CharField(primary_key=True, max_length=USERNAME_LENGTH)
    _password = models.CharField(max_length=PASSWORD_LENGTH)
    _is_manager = models.BooleanField(default=False)
    _name = models.CharField(max_length=100)
    
    def get_id(self):
        return self._username

    def get_name(self):
        return self._name

    def is_manager(self):
        return self._is_manager

    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.objects.get(_username=username, _password=password)
        except models.Model.DoesNotExist:
            return None