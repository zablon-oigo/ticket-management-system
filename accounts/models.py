from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from PIL import Image
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
        indexes=[
            models.Index(fields=['-user'])
        ]
    
    def __str__(self):
        return f'Profile of {self.user.email}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.photo.path)
        if img.height > 300 or img.width >300 :
            output_size=(300,200)
            img.thumbnail(output_size)
            img.save(self.photo.path)
