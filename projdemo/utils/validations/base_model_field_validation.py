from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


class BaseModelFieldValidation:

    def has_only_alphabet_validate(value:str):
        if not value.isalpha():
            raise ValidationError('Value must be in alphabet!')

    def has_only_alphabet_number_validate(value:str):
        if not re.match('^[a-zA-Z0-9 ]*$', value):
            raise ValidationError('Value must be only in alphabet & number!')