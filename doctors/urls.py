# doctors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('patient-records/', views.patient_records, name='patient_records'),
    # Add more URLs as needed
]
