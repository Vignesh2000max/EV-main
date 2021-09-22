from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from users import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'contact', 'is_manager']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username', 'firstname', 'lastname', 'contact', 'address', 'city', 'area', 'state', 'pin')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_manager')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.bookedSlotLogDetail)