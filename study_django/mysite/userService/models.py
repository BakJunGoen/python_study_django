from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    test = models.CharField(max_length=20, default="")
    test2 = models.CharField(max_length=20, null=True)
    first_name = None


# class Users(models.Model):
#     user_id = models.CharField(max_length=32, unique=True, verbose_name="user_id")
#     user_name = models.CharField(max_length=16, unique=True, verbose_name="user_name")
#     user_email = models.CharField(max_length=128, unique=True, verbose_name="user_email")
#     user_pw = models.CharField(max_length=128, verbose_name="user_pw")
#     user_is_staff = models.BooleanField(default=False, verbose_name="user_is_staff") #어드민 접속 가능 여부
#     user_last_login = models.DateTimeField(auto_now_add=True, verbose_name="user_last_login")# 유저 마지막 로그인
#     user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="user_register_dttm")# 아이디 만든시간



