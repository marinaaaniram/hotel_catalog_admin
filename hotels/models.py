from django.db import models
from django.db.models import RESTRICT

from references.models import City
from utils.validators import validate_phone_number


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20, validators=[validate_phone_number])
    city = models.ForeignKey(City, on_delete=RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
