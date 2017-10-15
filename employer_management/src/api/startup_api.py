from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.conf.urls import url
import datetime

from .api_base import ApiBase
from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine


# Create your views here.
class StartupViewSet(ModelViewSet, ApiBase):
    permission_classes = (AllowAny,)

    @classmethod
    def get_router(cls):
        urlpatterns = [
            url(r'ping/$', cls.as_view({'get': 'ping'})),
        ]

        return urlpatterns

    def ping(self, request, *args, **kwargs):
        now = datetime.datetime.utcnow()
        data = 'SERVER ON {0}'.format(now.strftime('%Y-%m-%d %H:%M'))

        return self.as_success(data)




