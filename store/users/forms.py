from django import forms
from . models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
        })
    )
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Введите имя'
        })
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Введите фамилию',
        })
    )
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
        'aria-describedby' : 'usernameHelp',
        })
    )
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
        'aria-describedby': 'emailHelp',
        })
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Введите пароль',
        })
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
        })
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'readonly' : True,
        })
    )
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control py-4',
        'readonly' : True,
        })
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'custom-file-input'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        })
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        })
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

