from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Admin, Salesman

# Register your models here.


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    """Admin for 'Admin' users in lambdaSystem."""
    list_display = ('pk', 'user', 'identification_document',
                    'name', 'created', 'last_modified')

    list_display_links = ('pk', 'user')


@admin.register(Salesman)
class SalesmanAdmin(admin.ModelAdmin):
    """Admin for Salesman users."""
    list_display = ('pk', 'user', 'identification_document',
                    'name', 'created', 'last_modified',
                    'count_sells', 'earnings', 'picture')

    list_editable = ('name', 'picture')


class UserAdmin(BaseUserAdmin):
    """User admin to make inline with other fields"""
    list_display = (
        'username',
        'password',
        'email',
    )
