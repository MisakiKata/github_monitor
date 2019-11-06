from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserList(AbstractUser):
    token = models.TextField(verbose_name='Token', blank=True)
    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.username
