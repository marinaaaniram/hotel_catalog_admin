import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    rule = re.compile(r'^(\+7)?\d{10}$')

    if not rule.search(value):
        raise ValidationError('Invalid phone number')