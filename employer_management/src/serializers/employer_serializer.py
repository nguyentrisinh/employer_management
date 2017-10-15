from rest_framework import serializers

from ..models import Employer


class BaseEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class PartTimeEmployerSerializer(serializers.ModelSerializer):
    day_salary = serializers.DecimalField(max_digits=15, decimal_places=1)

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id', 'day_salary')


class FullTimeEmployerSerializer(serializers.ModelSerializer):
    month_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    salary_level = serializers.FloatField()
    allowance = serializers.DecimalField(max_digits=15, decimal_places=1)

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id',
                  'month_salary', 'salary_level', 'allowance')


class EmployerFilterSerializer(serializers.ModelSerializer):
    month_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    salary_level = serializers.FloatField()
    allowance = serializers.DecimalField(max_digits=15, decimal_places=1)
    day_salary = serializers.DecimalField(max_digits=15, decimal_places=1)

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id',
                  'month_salary', 'salary_level', 'allowance', 'day_salary')


class MaxPartTimeEmployerSalarySerializer(serializers.ModelSerializer):
    day_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    total_salary = serializers.DecimalField(max_digits=15, decimal_places=1)

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id', 'day_salary', 'total_salary')


class MaxFullTimeEmployerSalarySerializer(serializers.ModelSerializer):
    month_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    salary_level = serializers.FloatField()
    allowance = serializers.DecimalField(max_digits=15, decimal_places=1)
    total_salary = serializers.DecimalField(max_digits=20, decimal_places=1)

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id',
                  'month_salary', 'salary_level', 'allowance', 'total_salary')


class EmployerListSalaryFilterSerializer(serializers.ModelSerializer):
    month_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    salary_level = serializers.FloatField()
    allowance = serializers.DecimalField(max_digits=15, decimal_places=1)
    day_salary = serializers.DecimalField(max_digits=15, decimal_places=1)
    total_salary = serializers.DecimalField(max_digits=20, decimal_places=1)
    working_day_number = serializers.IntegerField()

    class Meta:
        model = Employer
        fields = ('id', 'name', 'phone', 'birthday', 'department_id',
                  'month_salary', 'salary_level', 'allowance', 'day_salary', 'working_day_number', 'total_salary')

