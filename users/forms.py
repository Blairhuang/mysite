from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile #从当前数据库中提取profile 


class UserRegisterForm(UserCreationForm): #注册界面
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): #更新界面 model form & update user model, 即这个form 是针对于specific model 数据库
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']