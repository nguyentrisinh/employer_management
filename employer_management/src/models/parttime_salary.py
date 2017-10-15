from django.db import models
from .working_month import WorkingMonth
from .parttime_employer import ParttimeEmployer


class ParttimeSalary(models.Model):
    objects = models.Manager()

    working_day_number = models.PositiveSmallIntegerField()
    total_salary = models.DecimalField(max_digits=20, decimal_places=1)

    working_month_id = models.ForeignKey(WorkingMonth, on_delete=models.CASCADE,)
    part_time_employer_id = models.ForeignKey(ParttimeEmployer, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.total_salary