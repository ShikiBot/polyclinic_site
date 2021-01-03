from django.contrib import admin
from .models import Doctors_specialty, Social_status, Diagnosis, Pacient, Doctor, Treatment_history

class DoctorInline(admin.TabularInline):
    model = Doctor

class TreatmentHistoryInline(admin.TabularInline):
    model = Treatment_history

class PacientInline(admin.TabularInline):
    model = Pacient

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'qualification', 
        'doc_specialty'
    )
    fields = [
        'name', 
        (
            'doc_specialty', 
            'qualification'
        )
    ]            

@admin.register(Pacient)
class PacientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'date_of_birth', 
        'soc_status', 
        'condition', 
        'date_of_death'
    )
    fields = [
        'name', 
        'soc_status', 
        'condition', 
        (
            'date_of_birth', 
            'date_of_death'
        )
    ]
    list_filter = (
        'soc_status', 
        'condition'
    )

@admin.register(Treatment_history)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'pac_name', 
        'doc_name', 
        'diagnosis', 
        'ambulatory', 
        'dispensary', 
        'start_date_of_treatment', 
        'end_date_of_treatment'
    )
    list_filter = (
        'diagnosis', 
        'ambulatory', 
        'dispensary'
    )

@admin.register(Doctors_specialty)
class DoctorsSpecialtyAdmin(admin.ModelAdmin):
    inlines = [DoctorInline]

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    inlines = [TreatmentHistoryInline]

@admin.register(Social_status)
class SocialStatusAdmin(admin.ModelAdmin):
    inlines = [PacientInline]
