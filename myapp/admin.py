from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('city', 'phone', 'profile_pic'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('city', 'phone', 'profile_pic'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
