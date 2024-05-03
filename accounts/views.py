from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout, get_user_model
from .forms import RegisterCustomerForm,LoginForm,ProfileForm
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
        form=RegisterCustomerForm()
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request, email=email, password=password)

            if user is not None and user.is_active:
                login(request, user)
                messages.success(request,'Authenticated Successfully')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Invalid Email or Password')
                return redirect('login')
    else:
        form=LoginForm()
        context={'form':form}
        
    return render(request, 'accounts/login.html',context)
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout request was successfull')
    return redirect('login')

def profile_edit(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect("")
    else:
        form=ProfileForm()
    return render(request,'accounts/profile.html',{'form':form})