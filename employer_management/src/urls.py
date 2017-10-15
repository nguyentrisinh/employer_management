from django.conf.urls import url, include

from .api import StartupViewSet, DepartmentViewSet, EmployerViewSet, FulltimeSalaryViewSet, ParttimeSalaryViewSet, \
    WorkingMonthViewSet


urlpatterns = [
    url(r'^startup/', include(StartupViewSet.get_router(), namespace='startup')),
    url(r'^employers/', include(EmployerViewSet.get_router(), namespace='employer')),
    url(r'^departments/', include(DepartmentViewSet.get_router(), namespace='departments')),
    url(r'^full_time_salary/', include(FulltimeSalaryViewSet.get_router(), namespace='full time salary')),
    url(r'^part_time_salary/', include(ParttimeSalaryViewSet.get_router(), namespace='part time salary')),
    url(r'^working_month/', include(WorkingMonthViewSet.get_router(), namespace='working month')),
]

