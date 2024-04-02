from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from patients.models import Patient

@login_required
@permission_required('doctors.view_patient_records', raise_exception=True)
def patient_records(request):
    patients = Patient.objects.all()  # Query all patients
    return render(request, 'doctors/patient_records.html', {'patients': patients})