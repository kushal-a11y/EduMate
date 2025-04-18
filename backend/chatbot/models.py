from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    student_id = models.CharField(max_length=5, unique= True)
    mood = models.CharField(max_length=100, blank=True, null= True)
    sreak_days = models.IntegerField(default=0)
