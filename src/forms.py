from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Email"
    }))
    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    }))
    password2 = forms.CharField(max_length=50, label='Confirm password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm password"
    }))