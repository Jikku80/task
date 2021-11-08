# Generated by Django 3.2.9 on 2021-11-07 07:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('temporary_address', models.CharField(max_length=150)),
                ('permanent_address', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('alternate_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('emergency_contact_person', models.CharField(max_length=150)),
                ('emergency_contact_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('cv', models.FileField(upload_to='uploads/cv')),
                ('citizenship', models.ImageField(upload_to='uploads/citizenship')),
                ('driving_license', models.ImageField(upload_to='uploads/driving_license')),
                ('department', models.CharField(choices=[('Employee', 'Employee'), ('Department Head', 'Department Head'), ('Admin', 'Admin')], default='Employee', max_length=150)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('OFF', 'OFF')], default='Employee', max_length=150)),
                ('academy_level', models.CharField(choices=[('S.L.C', 'S.L.C'), ('+2', '+2'), ('Diploma', 'Diploma'), ('Bachelor', 'Bachelor'), ('Master', 'Master')], default='Diploma', max_length=100)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]