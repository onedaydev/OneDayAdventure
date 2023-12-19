from typing import Any
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import SetPasswordForm
from django.views.generic.edit import UpdateView
from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from users.forms import LoginForm, SignupForm, WithdrawForm, ProfileUpdateForm
from users.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "users/signup.html", context)


def profile_view(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "users/profile.html", context)


@login_required
def withdraw_view(request):
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data["password"]
            if request.user.check_password(pwd) and not request.user.is_staff:
                request.user.delete()
                messages.success(request, "Your account has been successfully deleted.")
                return redirect("/")
            else:
                form.add_error("password", "Incorrect password.")
    else:
        form = WithdrawForm()
    context = {
        "form": form,
    }
    return render(request, "users/withdraw.html", context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users:profile_update')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)

        password_form = SetPasswordForm(user=self.get_object(), data=self.request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(self.request, '프로필 및 비밀번호가 성공적으로 업데이트되었습니다.')

        return response
