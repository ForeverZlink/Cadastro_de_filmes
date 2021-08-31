from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validade_if_the_note_is_valid(value):
    if value>10 or value <0:
        raise ValidationError(
            _('Digite um nota entre 0 a 10.'),
            params={'value': value},
            )

