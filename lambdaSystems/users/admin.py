from django.contrib import admin

# Register your models here.
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user.profile.user')