from django.contrib import admin
from .models import User, user_type
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(user_type)

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')