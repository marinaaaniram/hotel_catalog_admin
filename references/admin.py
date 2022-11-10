from django import forms
from django.contrib import admin
from references.models import City


class CityAdminForm(forms.ModelForm):
    class Meta(object):
        model = City
        fields = '__all__'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('name',)