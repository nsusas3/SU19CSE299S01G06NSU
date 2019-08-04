from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user} Profile'
