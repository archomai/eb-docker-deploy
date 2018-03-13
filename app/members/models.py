from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # nickname 을 추가 (blank = true)
    img_profile = models.ImageField(upload_to='user', blank=True)
    nickname = models.CharField(max_length=50, blank=True)
