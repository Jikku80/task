from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'temporary_address', 'permanent_address', 'mobile_number', 'alternate_number', 'emergency_contact_person', 'emergency_contact_number', 'cv', 'citizenship', 'driving_license', 'department', 'status', 'academy_level', 'joining_date',)
        model = Employee