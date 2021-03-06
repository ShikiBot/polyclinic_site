# Generated by Django 3.1.3 on 2021-01-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardfile', '0002_auto_20210103_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['doc_specialty']},
        ),
        migrations.AlterModelOptions(
            name='pacient',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='pacient',
            name='condition',
            field=models.CharField(blank=True, choices=[('t', 'лечится'), ('c', 'вылечился'), ('h', 'направлен в стационар'), ('d', 'умер')], default='t', max_length=1, verbose_name='Состояние пациента:'),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рожения:'),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='date_of_death',
            field=models.DateField(blank=True, help_text='(необязательно)', null=True, verbose_name='Дата смерти:'),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ФИО:'),
        ),
        migrations.AlterField(
            model_name='social_status',
            name='status',
            field=models.CharField(help_text='Введите социальный статус пациента (учащийся, работающий, временно неработающий, инвалид, пенсионер)', max_length=200, verbose_name='Социальный статус:'),
        ),
    ]
