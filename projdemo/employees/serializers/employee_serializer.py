from employees.models.employee import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        rep['full_name'] = instance.get_full_name()
        rep['gender'] = 'Male' if instance.gender else 'Female'
        rep['status'] = 'Active' if instance.gender else 'Inactive'
        return rep

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'gender', 'dob', 'email', 'contact_no', 'bio', 'extra',
                  'status', 'created_at', 'updated_at', 'created_by', 'updated_by']
        extra_kwargs = {
            'first_name': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\' be null!',
                    'blank': 'can\' be blank!'
                }
            },
            'last_name': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\' be null!',
                    'blank': 'can\' be blank!',
                    # 'does_not_exist': 'Invalid country.'
                }
            },
            'email': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\' be null!',
                    'blank': 'can\' be blank!',
                    # 'does_not_exist': 'Invalid country.'
                }
            },
            'extra': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'write_only': True},
            'updated_by': {'write_only': True}
        }
