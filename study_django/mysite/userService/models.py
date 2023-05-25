from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# class User(models.Model):
#     user_id = models.CharField(max_length=32, unique=True, verbose_name="user_id")
#     user_name = models.CharField(max_length=16, unique=True, verbose_name="user_name")
#     user_email = models.CharField(max_length=128, unique=True, verbose_name="user_email")
#     user_pw = models.CharField(max_length=128, verbose_name="user_pw")
#     user_is_staff = models.BooleanField(default=False, verbose_name="user_is_staff") #어드민 접속 가능 여부
#     user_last_login = models.DateTimeField(auto_now_add=True, verbose_name="user_last_login")# 유저 마지막 로그인
#     user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="user_register_dttm")# 아이디 만든시간

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text