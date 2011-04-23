from django.db import models
from django.contrib.auth.models import User
from django import forms

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='get_profile_path', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='profile_thumb', blank=True, null=True, editable=False)
 # User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
