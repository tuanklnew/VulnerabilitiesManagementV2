from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

# Mac validator


def validate_mac_address(value):
    if not re.match(r"^([0-9a-fA-F]{2}([:-]?)){6}", value):
        raise ValidationError(
            _('%(value)s is not an MAC address'),
            params={'value': value},
        )