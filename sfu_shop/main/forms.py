# forms.py
from django import forms
from main.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'login-inp',
            'placeholder': 'Логин',
            'required': True
        })
    )
    
    password = forms.CharField(
        max_length=255,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'login-inp',
            'placeholder': 'Пароль',
            'required': True
        })
    
    )
    class Meta:
        model = User
        fields = ('username', 'password')
    def save(self, commit=True):
        # Здесь ваша логика сохранения
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        # Сохранение в базу данных
        from .models import User
        user_data = User.objects.create(
            username=username,
            password=password
        )
        
        return user_data