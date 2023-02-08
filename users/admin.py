from django.contrib import admin

from .models import CustomUser
from . models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type', ]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, UserModel)
admin.site.register(Member)
admin.site.register(Staff)
