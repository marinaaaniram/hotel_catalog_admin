from django import forms
from django.contrib import admin

from users.models import User


class UserAdminForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = '__all__'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('email', 'is_staff', 'is_superuser')
