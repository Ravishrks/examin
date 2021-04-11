from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True )
    avatar = models.ImageField(default="default.png", blank=True, null=True)
    bio = models.CharField(max_length=180, blank=True, null=True)

    # Educational background

    college = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    session_start = models.IntegerField(blank=True, null=True, default=2018)
    session_end = models.IntegerField(blank=True, null=True, default=2022)


    # Contact information

    phone = models.IntegerField(blank=True, null=True, default=0)
    address = models.CharField(max_length=100, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True, default=0)

    # General information

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not prefer to say', 'Not prefer to say'),
 
    )

    birthday =  models.DateTimeField(blank=True, null=True, auto_now_add=True)
    gender = models.CharField(max_length=20, choices=GENDER, null=True)
    


    
    def __str__(self):
        return f'{self.user}'


class PaymentDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True )
    is_due = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


