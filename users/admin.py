from django.contrib import admin
from .models import CustomUser


class User(admin.ModelAdmin):
    list_display = ('username', 'type', 'is_superuser', 'is_staff', 'is_active')


admin.site.register(CustomUser, User)
