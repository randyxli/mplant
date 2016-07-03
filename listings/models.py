from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.IntegerField()
    country = models.CharField(max_length=256) # i.e. USA, China
    administrative_area = models.CharField(max_length=256) # i.e. California, Fujian
    locality = models.CharField(max_length=1024) # i.e. San Francisco, Fuzhou
    location = models.CharField(max_length=1024) # ideally contains address or crossroad
    data = models.CharField(max_length=13172)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    template = models.CharField(max_length=8192)