from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
class CustomUser(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_engineer=models.BooleanField(default=False)
    email=models.EmailField(unique=True)

    class Meta:
        ordering=['-email']
    
    def __str__(self):
        return f'{self.email.lower()}'
    

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='profile/%Y', default='avatar.jpg')
    joined_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['-user']
    
    def __str__(self):
        return f'Profile of {self.user.email}'
