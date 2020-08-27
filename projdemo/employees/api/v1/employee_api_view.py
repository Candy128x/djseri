from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from employees.models.employee import Employee
from employees.serializers.employee_serializer import EmployeeSerializer
from rest_framework import status as http_status


class EmployeeListApiView(APIView):

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            id = (serializer.save()).id
            ret = Response({'created_with_id': id}, status=http_status.HTTP_201_CREATED)
        else:
            ret = Response(serializer.errors, http_status.HTTP_400_BAD_REQUEST)
        return ret

    def get(self, request):
        result = Employee.objects.all()
        result = EmployeeSerializer(result, many=True).data
        return Response(result)