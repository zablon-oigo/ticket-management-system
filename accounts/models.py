from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from PIL import Image
from .managers import CustomUserManager
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True,verbose_name='Email Address', max_length=255)
    first_name=models.CharField(verbose_name='First Name', max_length=30,blank=True )
    last_name=models.CharField(verbose_name='Last Name', max_length=30,blank=True )
    is_customer=models.BooleanField(default=False)
    is_engineer=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
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
