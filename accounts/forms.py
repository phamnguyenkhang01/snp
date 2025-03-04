from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'mobile', 'email', 'avatar', 'first_name', 'last_name', 'bio', 'dob', 'gender',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('mobile', 'email', 'avatar', 'first_name', 'last_name', 'bio', 'dob', 'gender',)
