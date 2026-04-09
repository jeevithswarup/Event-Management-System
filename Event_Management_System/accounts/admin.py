from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "username", "email", "phone_number", "is_staff", "is_active")
    search_fields = ("email", "username", "phone_number")
    ordering = ("id",)


admin.site.register(User, CustomUserAdmin)

