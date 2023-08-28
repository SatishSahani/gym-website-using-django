# gymwebsite/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('Sign in', views.home, name='home'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    # Add more URLs as needed
]
