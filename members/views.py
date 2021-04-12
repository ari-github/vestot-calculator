from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm, EditProfileForm, PasswordsChangeForm


class UserRegister(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')