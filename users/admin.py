from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'telegram_chat_id')
    search_fields = ('email', 'first_name', 'last_name', 'telegram_chat_id')
    list_filter = ('email', 'first_name', 'last_name', 'telegram_chat_id')
