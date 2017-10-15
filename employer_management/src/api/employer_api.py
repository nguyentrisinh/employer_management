from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api_base import ApiBase
from ..serializers import BaseEmployerSerializer, PartTimeEmployerSerializer, FullTimeEmployerSerializer
from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine
from ..services import EmployerServices
from ..models import Employer


# Create your views here.
class EmployerViewSet(ModelViewSet, ApiBase):
    permission_classes = (AllowAny,)
    serializer_class = BaseEmployerSerializer
    queryset = Employer.objects.all()

    employer_services = EmployerServices()

    @classmethod
    def get_router(cls):
        router = DefaultRouter()
        router.register(r'', cls)

        urlpatterns = [
            url(r'^part_time_employer/$', cls.as_view({
                'post': 'create_part_time_employer',
                'put': 'update_part_time_employer'
            })),
            url(r'^part_time_employer/(?P<employer_id>[0-9]+)$', cls.as_view({
                'put': 'update_part_time_employer'
            })),
            url(r'^full_time_employer/$', cls.as_view({
                'post': 'create_full_time_employer',
            })),
            url(r'^full_time_employer/(?P<employer_id>[0-9]+)$', cls.as_view({
                'put': 'update_full_time_employer'
            })),
            url(r'^filter_department/(?P<department_id>[0-9]+)$', cls.as_view({'get': 'get_by_department'})),
            url(r'^filter_employer_type/$', cls.as_view({
                'get': 'filter_employer_type'
            })),
            url(r'^get_all/$', cls.as_view({'get': 'get_all'})),
            url(r'^max_salary/(?P<working_month_id>[0-9]+)$', cls.as_view({'get': 'get_max_salary'})),

            url(r'', include(router.urls))
        ]

        return urlpatterns

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create_part_time_employer':
            return PartTimeEmployerSerializer

        if self.action == 'update_part_time_employer':
            return PartTimeEmployerSerializer

        if self.action == 'create_full_time_employer':
            return FullTimeEmployerSerializer

        if self.action == 'update_full_time_employer':
            return FullTimeEmployerSerializer

        return BaseEmployerSerializer

    def create_part_time_employer(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        birthday = request.data['birthday']
        day_salary = request.data['day_salary']
        department_id = request.data['department_id']

        result = self.employer_services.create_part_time_employer(name, phone, birthday, day_salary, department_id)
        return self.as_success(result)

    def update_part_time_employer(self, request, *args, **kwargs):
        employer_id = kwargs['employer_id']
        name = request.data['name']
        phone = request.data['phone']
        birthday = request.data['birthday']
        day_salary = request.data['day_salary']
        department_id = request.data['department_id']

        result = self.employer_services.update_part_time_employer(employer_id, name, phone, birthday, day_salary, department_id)
        return self.as_success(result)

    def create_full_time_employer(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        birthday = request.data['birthday']
        department_id = request.data['department_id']

        month_salary = request.data['month_salary']
        salary_level = request.data['salary_level']
        allowance = request.data['allowance']

        result = self.employer_services.create_full_time_employer(name=name, phone=phone,
                                                                  birthday=birthday, department_id=department_id,
                                                                  month_salary=month_salary, salary_level=salary_level,
                                                                  allowance=allowance)

        return self.as_success(result)

    def update_full_time_employer(self, request, *args, **kwargs):
        employer_id = kwargs['employer_id']
        name = request.data['name']
        phone = request.data['phone']
        birthday = request.data['birthday']
        department_id = request.data['department_id']

        month_salary = request.data['month_salary']
        salary_level = request.data['salary_level']
        allowance = request.data['allowance']

        result = self.employer_services.update_full_time_employer(employer_id=employer_id, name=name, phone=phone,
                                                                  birthday=birthday, department_id=department_id,
                                                                  month_salary=month_salary, salary_level=salary_level,
                                                                  allowance=allowance)

        return self.as_success(result)

    def get_by_department(self, request, *args, **kwargs):
        department_id = kwargs['department_id']

        result = self.employer_services.get_by_department(department_id)
        return self.as_success(result)

    def get_all(self, request, *args, **kwargs):
        result = self.employer_services.get_all()

        return self.as_success(result)

    def get_max_salary(self, request, *args, **kwargs):
        working_month_id = kwargs['working_month_id']
        result = self.employer_services.get_max_month_salary(working_month_id)

        return self.as_success(result)

    def filter_employer_type(self, request, *args, **kwargs):
        employer_type = request.GET.get('employer_type')
        working_month_id = request.GET.get('working_month_id')

        result = self.employer_services.get_list_salary_by_type(int(employer_type), int(working_month_id))

        return self.as_success(result)