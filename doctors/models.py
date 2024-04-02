from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Permission

class Doctor(AbstractUser):
    specialty = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('view_patient_records', 'Can view patient records'),
            # Add more permissions as needed
        ]

    def __str__(self):
        return self.username

