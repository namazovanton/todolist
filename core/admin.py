from django.contrib import admin
from django.db import models

from core.models import User


class AdminUser(admin.ModelAdmin):
    # username = models.CharField(max_length=30, unique=True)
    # email = models.EmailField(max_length=40, unique=True, null=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    list_display = ("username", "email", "first_name", "last_name")
    exclude = ("password",)
    list_filter = ["is_staff", "is_active", "is_superuser"]
    search_fields = ["first_name", "last_name", "username"]
    readonly_fields = ("last_login", "date_joined")


admin.site.register(User, AdminUser)
