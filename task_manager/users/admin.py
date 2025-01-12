from django.contrib import admin
from .models import User
from django.contrib.admin import DateFieldListFilter

admin.site.register(User)

'''@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'name', 'last_name', 'password', 'created_at')
    search_fields = ['name']
    list_filter = (('created_at', DateFieldListFilter),)
'''