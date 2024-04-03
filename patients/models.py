from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Add a field for the title
    diagnosis = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.title:  # Set the title if not provided
            self.title = f"{self.patient.name}'s Medical Record - {self.date_created.strftime('%Y-%m-%d')}"
        super().save(*args, **kwargs)


