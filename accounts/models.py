from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class UserDetails(AbstractBaseUser):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    contactno=models.CharField(max_length=12)
    dose1=models.FileField(null=True)
    dose2=models.FileField(null=True)
