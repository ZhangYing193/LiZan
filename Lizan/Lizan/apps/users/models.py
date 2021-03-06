from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """自定义用户模型"""
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True)

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
