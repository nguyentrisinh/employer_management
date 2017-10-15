from rest_framework import serializers

from ..models import FulltimeSalary, ParttimeSalary


class BaseFulltimeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = FulltimeSalary
        fields = '__all__'


class BaseParttimeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParttimeSalary
        fields = '__all__'