from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1' ,'password2')
        # widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control'})
        # }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Enter a Password'
        # self.fields['password1'].label=''
        # self.fields['password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>our password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Verify the Password'
        # self.fields['password2'].label=''
        # self.fields['password2'].help_text='<div class="form-text text-muted"><small>Enter the same password as before, for verification.</small></div>'


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields  = ('username', 'password')
      
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

