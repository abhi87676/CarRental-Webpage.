from django.shortcuts import render
from django.http import HttpResponse
from .models import Login, CarSignup

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if both name and password are provided
        if name and password:
            login_instance = Login(name=name, password=password)
            login_instance.save()
            return HttpResponse("Login successfully")
        else:
            return HttpResponse("Both name and password are required.")
    
    return render(request, 'login.html')

# 

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if all required fields are provided
        if name and email and password:
            signup_instance = CarSignup(name=name, email=email, password=password)
            signup_instance.save()
            return HttpResponse("Data is saved successfully")
        else:
            return HttpResponse("All fields are required.")

    return render(request, 'signup.html')

def join(request):
    return render(request, 'join.html')


#

