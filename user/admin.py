from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'is_organization')


admin.site.register(User, UserAdmin)
