from django.db import models

from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Employee(models.Model):

    LEVEL = (
    ("S.L.C", "S.L.C"),
    ("+2", "+2"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    )

    DEPARTMENT=(
        ("Employee", "Employee"),
        ("Department Head", "Department Head"),
        ("Admin", "Admin"),
    )

    STATUS=(
        ('Active', "Active"),
        ("OFF", "OFF"),
    )
  
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    temporary_address = models.CharField(max_length=150)
    permanent_address = models.CharField(max_length=150)
    mobileNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    mobile_number = models.CharField(validators = [mobileNumberRegex], max_length = 10, unique = True)
    altNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    alternate_number = models.CharField(validators = [altNumberRegex], max_length = 10, unique = True)
    emergency_contact_person = models.CharField(max_length=150)
    emergencyNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    emergency_contact_number = models.CharField(validators = [emergencyNumberRegex], max_length = 10, unique = True)
    cv = models.FileField(upload_to='uploads/cv')
    citizenship = models.ImageField(upload_to ='uploads/citizenship')
    driving_license = models.ImageField(upload_to ='uploads/driving_license')
    department = models.CharField(max_length=150, choices=DEPARTMENT, default='Employee')
    status = models.CharField(max_length=150, choices=STATUS, default='Employee')
    academy_level = models.CharField(max_length=100, choices=LEVEL, default='Diploma')
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


