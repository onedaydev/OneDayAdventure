from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from users.forms import (
    LoginForm,
    SignupForm,
    WithdrawForm,
    ProfileImageForm,
    CustomPasswordChangeForm,
)


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


@login_required
def profile_update_view(request):
    if request.method == "POST":
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        
        if image_form.is_valid() and password_form.is_valid():
            image_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # 중요: 비밀번호가 변경되면 세션을 업데이트합니다.
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        image_form = ProfileImageForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'users/profile_update.html', {
        'image_form': image_form,
        'password_form': password_form
    })  
