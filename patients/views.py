# patients/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, MedicalRecord

@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.user.healthcare_professional:
        medical_records = MedicalRecord.objects.filter(patient=patient)
        return render(request, 'patients/patient_detail.html', {'patient': patient, 'medical_records': medical_records})
    else:
        return render(request, 'error.html', {'message': 'You do not have permission to view this page.'})
