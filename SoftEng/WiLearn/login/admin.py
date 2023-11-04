from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Teachers
# Register your models here.


class TeachersAdmin(UserAdmin):
    ordering = ('username', 'first_name', 'last_name', 'email', 'password')
    list_display = ['username', 'email', 'first_name', 'last_name', ]
    fieldsets = (
        ("Teacher's Information", {'fields': ('first_name', 'last_name', 'username', 'email')}),
         )


admin.site.register(Teachers, TeachersAdmin)
