from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
User=get_user_model()

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','password1','password2']
    email=forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder':'Enter your email',
            'class':'px-6 py-4 w-full rounded-xl mb-2'
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter your password',
            'class':'w-full px-6 py-4 rounded-xl mb-2',
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Repeat your password',
            'class':'w-full px-6 py-4 rounded-xl mb-2'
        }))
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise  forms.ValidationError("Email is already taken")
        return email
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)