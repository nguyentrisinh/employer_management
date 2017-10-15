from rest_framework import serializers

from ..models import Department


class BaseDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'