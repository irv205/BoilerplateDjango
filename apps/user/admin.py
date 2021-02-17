from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'type', 'username', 'full_name', 'email', 'is_active')
    search_fields = ('id', 'email')

admin.site.register(User, UserAdmin)