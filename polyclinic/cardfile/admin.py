from django.contrib import admin
from .models import Doctors_specialty, Social_status, Diagnosis, Pacient, Doctor, Treatment_history

admin.site.register(Doctors_specialty)
admin.site.register(Social_status)
admin.site.register(Diagnosis)
admin.site.register(Pacient)
admin.site.register(Doctor)
admin.site.register(Treatment_history)
