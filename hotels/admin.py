from django import forms
from django.contrib import admin
from django.utils.html import format_html

from hotels.models import Hotel


class HotelAdminForm(forms.ModelForm):
    class Meta(object):
        model = Hotel
        fields = '__all__'


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    list_display = ('name', 'city', 'address', 'phone', 'city')