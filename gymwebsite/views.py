from django.shortcuts import render

# Create your views here.
# gymwebsite/views.py

from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')
