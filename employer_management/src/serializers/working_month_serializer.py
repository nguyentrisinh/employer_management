from rest_framework import serializers

from ..models import WorkingMonth


class BaseWorkingMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingMonth
        fields = '__all__'
