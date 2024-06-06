from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, MedicalRecordForm
from .models import Patient, MedicalRecord
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Patient
from django.db import models
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    patients = Patient.objects.all()
    return render(request, 'home.html', {'patients': patients})

@login_required
def edit_patient_view(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

@login_required
def add_patient_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

@login_required
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
def ventilator_control(request):
    return render(request, 'ventilator_control.html')

@login_required
def security_page(request):
    return render(request, 'security_control.html')

def medical_record_detail_view(request, patient_id, record_id):
    # Your view logic goes here
    pass  # Placeholder, replace with your actual view logic

@login_required
def patient_records(request):
    patients = Patient.objects.all()
    return render(request, 'patient_records.html', {'patients': patients})
@login_required
def patient_records(request):
    query = request.GET.get('query')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_records.html', {'patients': patients, 'query': query})
@login_required
def patient_management(request):
    # Assuming you have some logic here to fetch data or perform other operations
    # For now, we'll just render the template without passing any context data
    return render(request, 'patient_management.html')
@login_required
def remove_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return redirect('patient_records')

@login_required
def medical_record_view(request, patient_id, record_id):
    # Retrieve the medical record object from the database
    medical_record = get_object_or_404(MedicalRecord, pk=record_id)

    # Assuming you have a template named 'medical_record_detail.html'
    return render(request, 'medical_record_detail.html', {'medical_record': medical_record})

def search_patient(request):
    query = request.GET.get('query')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_records.html', {'patients': patients, 'query': query})