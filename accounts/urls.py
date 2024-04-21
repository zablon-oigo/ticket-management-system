from django.urls import path
from .views import (register_customer,login_user,logout_user)

urlpatterns=[
    path('register-customer/', register_customer, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]