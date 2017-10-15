from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from decimal import Decimal

from .api_base import ApiBase
from ..serializers import BaseParttimeSalarySerializer
from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine
from ..services import EmployerServices
from ..models import ParttimeSalary, ParttimeEmployer


# Create your views here.
class ParttimeSalaryViewSet(ModelViewSet, ApiBase):
    permission_classes = (AllowAny,)
    serializer_class = BaseParttimeSalarySerializer
    queryset = ParttimeSalary.objects.all()

    @classmethod
    def get_router(cls):
        router = DefaultRouter()
        router.register(r'', cls)

        urlpatterns = [
            url(r'', include(router.urls))
        ]

        return urlpatterns

    def create(self, request, *args, **kwargs):
        part_time_employer_id = request.data['part_time_employer_id']
        working_month_id = request.data['working_month_id']
        working_day_number = request.data['working_day_number']

        try:
            part_time_employer_id = ParttimeEmployer.objects.get(employer_id_id=part_time_employer_id)

            parttime_salary = ParttimeSalary.objects.filter(working_month_id=working_month_id,
                                                            part_time_employer_id=part_time_employer_id)

            if parttime_salary.exists():
                raise ApiCustomException(ErrorDefine.PART_TIME_SALARY_EXIST)

            total_salary = part_time_employer_id.day_salary * working_day_number

            request.data['part_time_employer_id'] = part_time_employer_id.id
            request.data['total_salary'] = round(total_salary, 1)
            res = super(ParttimeSalaryViewSet, self).create(request, args, kwargs)

            return self.as_success(res.data)

        except ParttimeEmployer.DoesNotExist:
            raise ApiCustomException(ErrorDefine.EMPLOYER_NOT_FOUND)