import random
import string
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

# from short_urls.models import URL


def get_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(7))


def create_short_url(instance):
    Cls = instance.__class__
    urls = [q['short'] for q in Cls.objects.values('short')]
    new_code = get_code()
    while new_code in urls:
        new_code = get_code()
    return new_code


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Invalid URL")
    return value
