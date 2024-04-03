from django import forms
from .models import MedicalRecord, Patient

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis']

class PatientForm(forms.ModelForm):
        class Meta:
            model = Patient
            fields = ['name', 'date_of_birth']