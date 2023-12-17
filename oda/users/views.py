from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Fail to Login")
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
        'user': user,
    }
    return render(request, "users/profile.html", context)