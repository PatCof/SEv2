from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Teachers
# Register your models here.


class TeachersAdmin(UserAdmin):
    ordering = ('username', 'first_name', 'last_name', 'email', 'password')
    list_display = ['first_name', 'last_name', 'username', 'email']
    fieldsets = (
        ("Teacher's Information", {'fields': ('first_name', 'last_name', 'username', 'email', 'password',)}),
         )


admin.site.register(Teachers, TeachersAdmin)
