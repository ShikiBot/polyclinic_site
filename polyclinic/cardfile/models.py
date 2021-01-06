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
        verbose_name='Специальность',
        max_length=200, 
        help_text="Введите специальность врача (терапевт, невропатолог и т.п.)")  

    class Meta:
        verbose_name='Специальность врача'  
        verbose_name_plural = 'Специальности врачей'    

    def __str__(self):
        return self.specialty

class Social_status(models.Model):
    """
    Модель, представляющая социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)
    """
    status = models.CharField(
        verbose_name='Социальный статус:',
        max_length=200, 
        help_text="Введите социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)")

    class Meta:
        verbose_name='Социальный статус пациента'
        verbose_name_plural = 'Социальные статусы пациентов' 

    def __str__(self):
        return self.status

class Diagnosis(models.Model):
    """
    Модель, представляющая диагноз (кариес, астма, пневмония и т.д.)
    """
    diagnosis = models.CharField(
        verbose_name='Диагноз',
        max_length=200, 
        help_text="Введите диагноз (кариес, астма, пневмония и т.д.)")

    class Meta:
        verbose_name='Диагноз'
        verbose_name_plural = 'Диагнозы' 

    def __str__(self):
        return self.diagnosis

class Pacient(models.Model):
    """
    Модель, представляющая пациента
    """
    name = models.CharField(
        verbose_name='ФИО пациента',
        max_length=200)

    date_of_birth = models.DateField(
        verbose_name='Дата рожения пациента',
        null=True, 
        blank=True)

    soc_status = models.ForeignKey(
        'Social_status',
        verbose_name='Социальный статус пациента', 
        on_delete=models.SET_NULL,
        null=True)

    PACIENT_CONDITION = (
        ('t', 'лечится'),
        ('c', 'вылечился'),
        ('h', 'направлен в стационар'),
        ('d', 'умер'),
    )

    condition = models.CharField(
        verbose_name='Состояние пациента',
        max_length=1, 
        choices=PACIENT_CONDITION, 
        blank=True, default='t')        

    date_of_death = models.DateField(
        verbose_name='Дата смерти пациента',
        null=True,
        blank=True,
        help_text='(необязательно)')

    class Meta:
        ordering = ['name']
        verbose_name='Пациент'
        verbose_name_plural = 'Пациенты' 

    def get_absolute_url(self):
        return reverse('pacient-detail', args=[str(self.id)])


    def __str__(self):
        return self.name

class Doctor(models.Model):
    """
    Модель, представляющая врача
    """
    name = models.CharField(
        verbose_name='ФИО врача',
        max_length=200) 

    user = models.ForeignKey(
        User,
        verbose_name='Username врача', 
        on_delete=models.SET_NULL,
        null=True)

    QUALIFICATION_LEVEL = (
        ('2', 'Вторая квалификационная категория'),
        ('1', 'Первая квалификационная категория'),
        ('0', 'Высшая квалификационная категория'),
    )

    qualification = models.CharField(
        verbose_name='Квалификация врача',
        max_length=1, 
        choices=QUALIFICATION_LEVEL, 
        blank=True,
        default='2') 

    doc_specialty = models.ForeignKey(
        'Doctors_specialty',
        verbose_name='Специальность врача', 
        on_delete=models.SET_NULL,
        null=True) 
    
    class Meta:
        ordering = ['doc_specialty']
        verbose_name='Врач'
        verbose_name_plural = 'Врачи' 
        permissions = (("can_add_doctor", "Can add doctor"),)

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.id)])


    def __str__(self):
        return '{0} ({1} - {2})'.format(self.name, self.doc_specialty, self.QUALIFICATION_LEVEL[2-int(self.qualification)][1])

class Treatment_history(models.Model):
    """
    Модель, представляющая историю лечений пациентов
    """

    pac_name = models.ForeignKey(
        'Pacient',
        verbose_name='Пациент',
        on_delete=models.SET_NULL,
        null=True)  

    doc_name = models.ForeignKey(
        'Doctor', 
        verbose_name='Лечащий врач',
        on_delete=models.SET_NULL,
        null=True) 

    diagnosis = models.ForeignKey(
        'Diagnosis', 
        verbose_name='Диагноз',
        on_delete=models.SET_NULL,
        null=True) 

    description = models.TextField(
        verbose_name='Симптомы',
        max_length=1000)

    ambulatory = models.BooleanField(verbose_name='Амбулаторное лечение')

    dispensary = models.BooleanField(verbose_name='Диспансерный учет')

    start_date_of_treatment = models.DateField(
        verbose_name='Дата начала лечения',
        null=True,
        blank=True)

    end_date_of_treatment = models.DateField(
        verbose_name='Дата окончания лечения',
        null=True,
        blank=True)
    
    class Meta:
        ordering = ['start_date_of_treatment']
        verbose_name='История лечения'
        verbose_name_plural = 'Истории лечений'

    def get_absolute_url(self):
        return reverse('treatment_history_detail', args=[str(self.id)])


    def __str__(self):
        return '{0} : {1} ({2})'.format(self.start_date_of_treatment, self.pac_name.name, self.diagnosis)