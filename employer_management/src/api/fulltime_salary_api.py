from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from decimal import Decimal

from .api_base import ApiBase
from ..serializers import BaseFulltimeSalarySerializer
from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine
from ..services import EmployerServices
from ..models import FulltimeSalary, FulltimeEmployer, WorkingMonth


# Create your views here.
class FulltimeSalaryViewSet(ModelViewSet, ApiBase):
    permission_classes = (AllowAny,)
    serializer_class = BaseFulltimeSalarySerializer
    queryset = FulltimeSalary.objects.all()

    @classmethod
    def get_router(cls):
        router = DefaultRouter()
        router.register(r'', cls)

        urlpatterns = [
            url(r'', include(router.urls))
        ]

        return urlpatterns

    def create(self, request, *args, **kwargs):
        full_time_employer_id = request.data['full_time_employer_id']
        working_month_id = request.data['working_month_id']

        try:
            full_time_employer_id = FulltimeEmployer.objects.get(employer_id_id=full_time_employer_id)

            fulltime_salary = FulltimeSalary.objects.filter(working_month_id=working_month_id,
                                                            full_time_employer_id=full_time_employer_id)

            if fulltime_salary.exists():
                raise ApiCustomException(ErrorDefine.FULL_TIME_SALARY_EXIST)

            total_salary = full_time_employer_id.month_salary * Decimal(full_time_employer_id.salary_level) \
                           + full_time_employer_id.allowance

            request.data['full_time_employer_id'] = full_time_employer_id.id
            request.data['total_salary'] = round(total_salary, 1)
            res = super(FulltimeSalaryViewSet, self).create(request, args, kwargs)

            return self.as_success(res.data)
        except FulltimeEmployer.DoesNotExist:
            raise ApiCustomException(ErrorDefine.EMPLOYER_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        salary_id = kwargs['pk']
        full_time_employer_id = request.data['full_time_employer_id']
        working_month_id = request.data['working_month_id']

        try:
            full_time_employer_id = FulltimeEmployer.objects.get(employer_id_id=full_time_employer_id)

            fulltime_salary = FulltimeSalary.objects.filter(working_month_id=working_month_id,
                                                            full_time_employer_id=full_time_employer_id)\
                .exclude(id=salary_id)

            if fulltime_salary.exists():
                raise ApiCustomException(ErrorDefine.FULL_TIME_SALARY_EXIST)

            total_salary = full_time_employer_id.month_salary * Decimal(full_time_employer_id.salary_level) \
                           + full_time_employer_id.allowance

            request.data['full_time_employer_id'] = full_time_employer_id.id
            request.data['total_salary'] = round(total_salary, 1)
            res = super(FulltimeSalaryViewSet, self).update(request, args, kwargs)

            return self.as_success(res.data)
        except FulltimeEmployer.DoesNotExist:
            raise ApiCustomException(ErrorDefine.EMPLOYER_NOT_FOUND)