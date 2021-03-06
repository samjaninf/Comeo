from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.crowdfunding.models import Campaign, Transaction
from apps.profiles.forms import AdminUserChangeForm, AdminUserCreationForm
from apps.profiles.models import ComeoUser, Profile


class CustomUserAdmin(UserAdmin):
    # Forms necessary to add and change user instances
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(ComeoUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Transaction, list_display=('date_created',))
admin.site.register(Campaign, list_display=('desc_headline', 'date_created',
                                            'date_start', 'date_finish', 'state'))
