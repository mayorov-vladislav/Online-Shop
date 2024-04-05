from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import *


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
            model = User
            fields = [
                'username',
                'password',
            ]








            
    # username = forms.CharField(
    #     label = "Имя",
    #     widget = forms.TextInput(attrs={"autofoucs": True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите ваше имя пользователя',
    #                                   })
    #     )
    # password = forms.CharField(
    #     label = "Пароль",
    #     widget = forms.PasswordInput(attrs={"autocopmlete": "current-poassword",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль',
    #                                       }),
    #     )

    