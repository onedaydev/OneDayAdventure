from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", 'password')}),
        ("Private Info", {"fields": ("first_name", "last_name", "email")}),
        ("Image",{"fields":("profile_image",)}),
        ("Authority",{"fields":("is_active","is_staff","is_superuser")}),
        ("Date",{"fields":("last_login","date_joined")}),
    ]
