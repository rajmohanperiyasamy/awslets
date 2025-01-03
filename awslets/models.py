from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return self.user.username



class Contact(models.Model):
    name = models.CharField( max_length=150)
    email = models.EmailField()
    Mobile = models.CharField(max_length=13,default='')
    message = models.TextField()

    def __str__(self):
        return self.email