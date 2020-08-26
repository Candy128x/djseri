from django.db import models
from utils.models.base import Base


class GenderChoices(models.IntegerChoices):
    FEMALE = 0
    MALE = 1


# Create your models here.
class Employee(Base):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, default=GenderChoices.MALE)
    dob = models.DateField(null=True, blank=True)
    email = models.CharField(null=False, blank=False, max_length=255)
    contact_no = models.CharField(default=None, null=True, blank=True, max_length=18)
    bio = models.CharField(default=None, null=True, blank=True, max_length=2048)
    extra = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.email

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
