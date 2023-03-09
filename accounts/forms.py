from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Login')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               strip=False,
                               required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password confirm',
                                       strip=False,
                                       required=True,
                                       widget=forms.PasswordInput)
    first_name = forms.CharField(label='First name', max_length=50, min_length=2, required=True)
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')
