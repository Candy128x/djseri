from django.db import models
from utils.models.base import Base, StatusBase
from django.core.validators import MinLengthValidator, RegexValidator
from utils.validations.base_model_field_validation import BaseModelFieldValidation
from django.forms import ModelForm


class GenderChoices(models.IntegerChoices):
    FEMALE = 0
    MALE = 1


# Create your models here.
class Employee(StatusBase):
    first_name = models.CharField(null=False, blank=False, max_length=255,
                                  validators=[MinLengthValidator(3),
                                              BaseModelFieldValidation.has_only_alphabet_validate],
                                  error_messages={'required': 'is required! (msg from model)'})
    last_name = models.CharField(null=False, blank=False, max_length=255,
                                 validators=[MinLengthValidator(3),
                                             BaseModelFieldValidation.has_only_alphabet_validate])
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, default=GenderChoices.MALE)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=255,
                              error_messages={'unique': 'must be unique!'})
    contact_no = models.CharField(default=None, null=True, blank=True, max_length=18)
    bio = models.CharField(default=None, null=True, blank=True, max_length=2048,
                           validators=[BaseModelFieldValidation.has_only_alphabet_number_validate])
    extra = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'employees'
        ordering = ['-id']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize()


class EmployeeModelForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name']
        error_messages = {
            'first_name': {
                'required': "is required! (msg from model form)",
            },
        }