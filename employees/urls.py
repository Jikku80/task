from django.urls import path

from .views import AddEmployee, EmployeeList, EmployeeDetail, EditEmployee, SearchEmployee

urlpatterns = [
    path('<int:pk>/', EmployeeDetail.as_view()),
    path('listemployee/', EmployeeList.as_view()),
    path('addemployee/', AddEmployee.as_view()),
    path('<int:pk>/editemployee/', EditEmployee.as_view()),
    path('searchemployee/', SearchEmployee.as_view()),
]
