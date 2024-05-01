# patients/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.shortcuts import render, get_object_or_404
from .models import MedicalRecord

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from .models import Patient, MedicalRecord
from .forms import MedicalRecordForm, PatientForm


@login_required
def edit_patient_view(request, patient_id):
    # Retrieve the patient object from the database
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()  # Save the form data to update the patient object
            return redirect('home')  # Redirect to home page after successful edit
    else:
        # Create a form instance and populate it with the patient's current data
        form = PatientForm(instance=patient)

    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

@login_required
def add_patient_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful addition
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})
@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful addition
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})


def patient_detail_view(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    medical_records = patient.medicalrecord_set.all()

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = patient
            medical_record.save()
            return redirect('patient_detail', patient_id=patient_id)
    else:
        form = MedicalRecordForm()

    return render(request, 'patient_detail.html', {'patient': patient, 'medical_records': medical_records, 'form': form})


@login_required
def medical_record_view(request, patient_id, record_id=None):
    patient = get_object_or_404(Patient, pk=patient_id)
    medical_records = patient.medicalrecord_set.all()

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = patient
            medical_record.save()
            return redirect('patient_detail', patient_id=patient_id)
    else:
        form = MedicalRecordForm()

    return render(request, 'patient_detail.html', {'patient': patient, 'medical_records': medical_records, 'form': form})
def patient_records(request):
    # Retrieve patient records from the database or any other source
    # Implement your logic here
    return render(request, 'patient_records.html', context)

def medical_record_detail_view(request, patient_id, record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=record_id)
    return render(request, 'medical_record_detail.html', {'medical_record': medical_record})

def ventilator_control(request):
    # You can add logic here to handle ventilator control settings
    return render(request, 'ventilator_control.html')
def security_page(request):
    return render(request, 'security_control.html')