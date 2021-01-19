from django.db import models

# Create your models here.
class User(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    name_ko = models.CharField(max_length=20)
    name_eng = models.CharField(max_length=20)
    call = models.CharField(max_length=15)
    passport = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    birthday = models.IntegerField()
    sex = models.IntegerField()