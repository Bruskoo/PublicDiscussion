from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, verbose_name="о себе")
    is_organization = models.BooleanField(default=False, verbose_name="организация")

    def __str__(self):
        return self.username
