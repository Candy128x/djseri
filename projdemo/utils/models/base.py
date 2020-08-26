from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField(default='system', max_length=255)
    updated_by = models.CharField(default='system', max_length=255)

    class Meta:
        abstract = True


class StatusBase(Base):
    INACTIVE = 0
    ACTIVE = 1

    STATUS_CHOICES = [
        (INACTIVE, 'inactive'),
        (ACTIVE, 'active')
    ]

    status = models.IntegerField(default=ACTIVE, choices=STATUS_CHOICES)

    class Meta:
        abstract = True
