# Generated by Django 3.1.3 on 2021-01-03 08:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(help_text='Введите диагноз (кариес, астма, пневмония и т.д.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualification', models.CharField(blank=True, choices=[('2', 'Вторая квалификационная категория'), ('1', 'Первая квалификационная категория'), ('0', 'Высшая квалификационная категория')], default='2', help_text='Квалификация врача', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors_specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(help_text='Введите специальность врача (терапевт, невропатолог и т.п.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(blank=True, choices=[('t', 'лечится'), ('c', 'вылечился'), ('h', 'направлен в стационар'), ('d', 'умер')], default='t', help_text='состояние пациента', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Social_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='Введите социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment_history',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Введите описание болезни пациента', max_length=1000)),
                ('ambulatory', models.BooleanField(help_text='Требуется ли пациенту амбулаторное лечение?')),
                ('dispensary', models.BooleanField(help_text='Состоит ли пациент на диспансерном учете?')),
                ('start_date_of_treatment', models.DateField(blank=True, help_text='Дата начала лечения', null=True)),
                ('end_date_of_treatment', models.DateField(blank=True, help_text='Дата конца лечения', null=True)),
                ('date_of_death', models.DateField(blank=True, help_text='Дата смерти (необязательно)', null=True, verbose_name='Died')),
                ('diagnosis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardfile.diagnosis')),
                ('doc_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardfile.doctor')),
                ('pac_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardfile.pacient')),
            ],
        ),
        migrations.AddField(
            model_name='pacient',
            name='soc_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardfile.social_status'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doc_specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardfile.doctors_specialty'),
        ),
    ]