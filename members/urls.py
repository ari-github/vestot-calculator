from django.urls import path
from django.contrib.auth import views

from .views import UserRegister, UserEdit, PasswordsChangeView, password_success
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success, name='password_success'),
]