from rest_framework import generics, permissions
from rest_framework import filters

from .models import Employee
from .permissions import IsAuthorOrReadOnly
from .serializers import EmployeeSerializer


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AddEmployee(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EditEmployee(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SearchEmployee(generics.ListAPIView):
    search_fields = ['first_name', 'last_name', 'department', 'joining_date']
    filter_backends = (filters.SearchFilter,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
