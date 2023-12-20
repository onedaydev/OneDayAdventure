from django.urls import path
from users.views import (
    login_view,
    logout_view,
    signup_view,
    profile_view,
    withdraw_view,
    profile_update_view,
)


app_name = "users"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("withdraw/", withdraw_view, name="withdraw"),
    path("profileupdate", profile_update_view, name="profile_update"),
]
