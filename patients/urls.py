from django.urls import path
from . import views
from .views import (
    add_patient_view,
    edit_patient_view,
    patient_detail_view,
    medical_record_detail_view,
    patient_records,
    ventilator_control,
    security_page,
    logout_view,
    search_patient,  # Import the search_patient view
    medical_record_view  # Import the MedicalRecordView class
)

urlpatterns = [
    path('add/', add_patient_view, name='add_patient'),
    path('<int:patient_id>/edit/', edit_patient_view, name='edit_patient'),
    path('patients/<int:patient_id>/', patient_detail_view, name='patient_detail'),
    path('patients/<int:patient_id>/medical-records/<int:record_id>/', medical_record_detail_view, name='medical_record_detail'),
    path('patient-records/', patient_records, name='patient_records'),
    path('ventilator/control/', ventilator_control, name='ventilator_control'),
    path('security/', security_page, name='security_control'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_patient, name='search_patient'),  # Correctly include the search_patient URL pattern
    path('management/', views.patient_management, name='patient_management'),  # Corrected the view function name
    path('patients/remove/<int:patient_id>/', views.remove_patient, name='remove_patient'),
    path('patients/<int:patient_id>/records/<int:record_id>/', views.medical_record_view, name='medical_record_view'),
    # Other URL patterns...
]
