from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True )
    avatar = models.ImageField(default="default.png", blank=True, null=True)
    bio = models.CharField(max_length=180, blank=True, null=True)

    
    def __str__(self):
        return f'{self.user}'

