from django import forms
from django.contrib import admin
from hotels.models import Hotel


class HotelAdminForm(forms.ModelForm):
    class Meta(object):
        model = Hotel
        fields = '__all__'


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    list_display = ('name', 'city', 'address', 'phone', 'city')