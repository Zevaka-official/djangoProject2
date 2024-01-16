from django.contrib import admin

from users_app.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_staff', 'is_active', 'email', 'phone')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')  # Add search


