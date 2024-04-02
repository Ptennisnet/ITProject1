# patients/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm


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
    return render(request, 'patient_detail.html', {'patient': patient})
