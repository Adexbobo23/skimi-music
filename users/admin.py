from django.contrib import admin
from .models import UserAccount


class UserAdmin(admin.ModelAdmin):
    search_fields  = ['full_name', 'username', 'email',  'phone']
    list_display  = ['full_name', 'username', 'email',  'phone']

admin.site.register(UserAccount, UserAdmin)