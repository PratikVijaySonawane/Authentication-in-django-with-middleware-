from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import auth,guest

# Creating the function for the Register
@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        intial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial = intial_data)
    return render(request,'register.html',{'form':form})    

#Creating the function for the login
@guest 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        intial_data = {'username':'','password':''}
        form = AuthenticationForm(initial = intial_data)
    return render(request,'login.html',{'form':form})

#Creating the function for the logout
def logout_view(request):
    logout(request)
    return redirect('login')

#Creating the function for the Dashboard
@auth #applying the dacorators
def dashboard_view(request):
    return render(request,"dashboard.html")