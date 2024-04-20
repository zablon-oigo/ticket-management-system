from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout, get_user_model
from .forms import RegisterCustomerForm

User=get_user_model()

def register_customer(request):
    if request.method =='POST':
        form=RegisterCustomerForm(request.POST)
        if form.is_valid():
            cd=form.save(commit=False)
            cd.is_customer=True
            cd.save()
            messages.success(request,'Account created. Please log in')
            return redirect('login')
        else:
            messages.error(request,"Please correct the Error .")
            return redirect("register-customer")
    else:
        form=RegisterCustomerForm()
        return render(request,'accounts/register.html',{'form':form})
