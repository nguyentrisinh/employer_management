# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Department, Employer, FulltimeEmployer, ParttimeEmployer, WorkingMonth, ParttimeSalary, \
    FulltimeSalary

# Register your models here.
admin.site.register(Department)
admin.site.register(Employer)
admin.site.register(FulltimeEmployer)
admin.site.register(ParttimeEmployer)
admin.site.register(WorkingMonth)
admin.site.register(ParttimeSalary)
admin.site.register(FulltimeSalary)
