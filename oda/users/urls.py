from django.urls import path
from users.views import (
    login_view,
    logout_view,
    signup_view,
    profile_view,
    withdraw_view,
    ProfileUpdateView,
)


app_name = "users"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("withdraw/", withdraw_view, name="withdraw"),
    # path("profile_image_update", ProfileImageUpdateView.as_view(), name="profile_image_update"),
    # path("password/change", ProfileUpdateView.as_view(), name="password_change"),
]
