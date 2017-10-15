from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api_base import ApiBase
from ..serializers import BaseDepartmentSerializer
from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine
from ..services import EmployerServices
from ..models import Department


class DepartmentViewSet(ModelViewSet, ApiBase):
    permission_classes = (AllowAny,)
    serializer_class = BaseDepartmentSerializer
    queryset = Department.objects.all()

    @classmethod
    def get_router(cls):
        router = DefaultRouter()
        router.register(r'', cls)

        urlpatterns = [
            url(r'', include(router.urls))
        ]

        return urlpatterns