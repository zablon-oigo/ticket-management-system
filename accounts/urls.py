from django.urls import path
from .views import (register_customer,login_user,logout_user)

urlpatterns=[
    path('', login_user, name='login'),
    path('register-customer/', register_customer, name='register'),
    path('logout/', logout_user, name='logout'),
]