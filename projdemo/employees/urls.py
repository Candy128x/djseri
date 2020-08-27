from django.urls import path
from employees.api.v1.employee_api_view import EmployeeListApiView

urlpatterns = [
    path('api/v1/', EmployeeListApiView.as_view()),
]