from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False)


    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'email'
        )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')



    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

