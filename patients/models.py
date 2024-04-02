from django.db import models
from django.contrib.auth.models import AbstractUser
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient.name}'s Medical Record"



