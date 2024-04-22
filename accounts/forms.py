from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
User=get_user_model()

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','password1','password2']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)