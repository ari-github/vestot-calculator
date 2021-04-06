from django.urls import path
from django.contrib.auth import views

from .views import UserRegister
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
]