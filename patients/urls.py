# patients/urls.py

from django.urls import path
from .views import add_patient_view, edit_patient_view, patient_detail_view  # Import the edit_patient_view

urlpatterns = [
    path('add/', add_patient_view, name='add_patient'),
    path('<int:patient_id>/edit/', edit_patient_view, name='edit_patient'),  # Define the URL pattern for editing a patient
    path('<int:patient_id>/', patient_detail_view, name='patient_detail'),
]