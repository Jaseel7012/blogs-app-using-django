from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    address=forms.CharField(max_length=100)
    
    class Meta:
        model= User
        fields=['username','address','email','password1','password2']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm,self).__init__(*args, **kwargs)
        for field in ['username','email','password2']:
            self.fields[field].help_text =None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','email']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserUpdateForm,self).__init__(*args, **kwargs)
        for field in ['username','email']:
            self.fields[field].help_text =None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['image']