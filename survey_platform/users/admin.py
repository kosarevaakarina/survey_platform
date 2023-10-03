from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Административная панель для модели User"""
    list_display = ('first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Персональные данные', {'fields': ('first_name', 'last_name')}),
        ('Активность пользователя', {'fields': ('is_active',)}),
        ('Права доступа', {'fields': ('is_staff', 'is_superuser', 'groups')}),
    )