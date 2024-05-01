from django.urls import path
from .views import add_patient_view, edit_patient_view, patient_detail_view, medical_record_view, patient_records
from . import views
urlpatterns = [
    path('add/', add_patient_view, name='add_patient'),
    path('<int:patient_id>/edit/', edit_patient_view, name='edit_patient'),
    path('patients/<int:patient_id>/', views.patient_detail_view, name='patient_detail'),
    # Ensure that the URL pattern accepts both patient_id and record_id
    path('patients/<int:patient_id>/medical-records/<int:record_id>/', views.medical_record_detail_view, name='medical_record_detail'),
    path('patient-records/', patient_records, name='patient_records'),
    path('patients/<int:patient_id>/medical-records/<int:record_id>/', views.medical_record_view,
         name='medical_record_view'),
    path('ventilator/control/', views.ventilator_control, name='ventilator_control'),
    path('security/', views.security_page, name='security_control'),

]