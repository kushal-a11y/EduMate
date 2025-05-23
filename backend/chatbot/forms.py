from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'student_id', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass