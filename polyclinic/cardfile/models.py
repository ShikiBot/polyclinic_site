from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Doctors_specialty(models.Model):
    """
    Модель, представляющая специальность врача (терапевт, невропатолог и т.п.)
    """
    specialty = models.CharField(
        max_length=200, 
        help_text="Введите специальность врача (терапевт, невропатолог и т.п.)")

    def __str__(self):
        return self.specialty

class Social_status(models.Model):
    """
    Модель, представляющая социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)
    """
    status = models.CharField(
        'Социальный статус:',
        max_length=200, 
        help_text="Введите социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)")

    def __str__(self):
        return self.status

class Diagnosis(models.Model):
    """
    Модель, представляющая диагноз (кариес, астма, пневмония и т.д.)
    """
    diagnosis = models.CharField(
        max_length=200, 
        help_text="Введите диагноз (кариес, астма, пневмония и т.д.)")

    def __str__(self):
        return self.diagnosis

class Pacient(models.Model):
    """
    Модель, представляющая пациента
    """
    name = models.CharField(
        'ФИО:',
        max_length=200)

    date_of_birth = models.DateField(
        'Дата рожения:',
        null=True, 
        blank=True)

    soc_status = models.ForeignKey(
        'Social_status', 
        on_delete=models.SET_NULL,
        null=True)

    PACIENT_CONDITION = (
        ('t', 'лечится'),
        ('c', 'вылечился'),
        ('h', 'направлен в стационар'),
        ('d', 'умер'),
    )

    condition = models.CharField(
        'Состояние пациента:',
        max_length=1, 
        choices=PACIENT_CONDITION, 
        blank=True, default='t')        

    date_of_death = models.DateField(
        'Дата смерти:',
        null=True,
        blank=True,
        help_text='(необязательно)')

    def get_absolute_url(self):
        return reverse('pacient-detail', args=[str(self)])


    def __str__(self):
        return self.name

class Doctor(models.Model):
    """
    Модель, представляющая врача
    """
    name = models.CharField(max_length=200) 

    QUALIFICATION_LEVEL = (
        ('2', 'Вторая квалификационная категория'),
        ('1', 'Первая квалификационная категория'),
        ('0', 'Высшая квалификационная категория'),
    )

    qualification = models.CharField(
        max_length=1, 
        choices=QUALIFICATION_LEVEL, 
        blank=True,
        default='2', 
        help_text='Квалификация врача') 

    doc_specialty = models.ForeignKey(
        'Doctors_specialty', 
        on_delete=models.SET_NULL,
        null=True) 

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self)])


    def __str__(self):
        return '{0} ({1} - {2})'.format(self.name, self.doc_specialty, self.QUALIFICATION_LEVEL[2-int(self.qualification)][1])

class Treatment_history(models.Model):
    """
    Модель, представляющая историю лечений пациентов
    """    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4)

    pac_name = models.ForeignKey(
        'Pacient', 
        on_delete=models.SET_NULL,
        null=True)  

    doc_name = models.ForeignKey(
        'Doctor', 
        on_delete=models.SET_NULL,
        null=True) 

    diagnosis = models.ForeignKey(
        'Diagnosis', 
        on_delete=models.SET_NULL,
        null=True) 

    description = models.TextField(max_length=1000, help_text="Введите описание болезни пациента")

    ambulatory = models.BooleanField(help_text="Требуется ли пациенту амбулаторное лечение?")

    dispensary = models.BooleanField(help_text="Состоит ли пациент на диспансерном учете?")

    start_date_of_treatment = models.DateField(
        null=True,
        blank=True,
        help_text='Дата начала лечения')

    end_date_of_treatment = models.DateField(
        null=True,
        blank=True,
        help_text='Дата конца лечения')

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.id)])


    def __str__(self):
        return '{0} : {1} ({2})'.format(self.start_date_of_treatment, self.pac_name.name, self.diagnosis)