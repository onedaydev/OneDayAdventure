from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

from users.models import User


class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": ("아이디 또는 비밀번호가 올바르지 않습니다. 다시 시도해주세요."),
        "inactive": ("계정이 비활성화 되었습니다."),
    }


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


class WithdrawForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class ProfileUpdateForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["profile_image"]
