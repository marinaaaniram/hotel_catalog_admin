from django.db import models
from django.db.models import RESTRICT
from django.core import validators
from references.models import City


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(validators=[validators.validate_email])
    phone = models.CharField(max_length=20, validators=[validators.RegexValidator(r'^(\+7)?\d{10}$')])
    city = models.ForeignKey(City, db_index=True, on_delete=RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'city', 'address')
