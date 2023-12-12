from django import forms
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "ID"},
        ),
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Password"},
        ),
    )


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"{username} is already used")
        return username

    def clean(self):
        password = self.cleaned_data["password"]
        password_check = self.cleaned_data["password_check"]
        if password != password_check:
            self.add_error("password_check", "password are not same")

    def save(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        profile_image = self.cleaned_data["profile_image"]
        user = User.objects.create_user(
            username=username,
            password=password,
            profile_image=profile_image,
        )
        return user
