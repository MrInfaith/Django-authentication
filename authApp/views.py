from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import auth,guest
# Create your views here.
@guest
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        intial_data={'username':'','password':''}
        form=AuthenticationForm(initial=intial_data)
    return render(request,'authApp/login.html',{'form':form})

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
        else:
            return render(request, 'authApp/registration.html', {'form': form})
    else:
        intial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=intial_data)
        return render(request,'authApp/registration.html',{'form':form})
@auth    
def home_view(request):
    return render(request,'authApp/home.html')

def logout_view(request):
    logout(request)
    return redirect('login') 