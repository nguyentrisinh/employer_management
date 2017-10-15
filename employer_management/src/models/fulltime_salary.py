from django.db import models
from .working_month import WorkingMonth
from .fulltime_employer import FulltimeEmployer


class FulltimeSalary(models.Model):
    objects = models.Manager()

    total_salary = models.DecimalField(max_digits=20, decimal_places=1)

    working_month_id = models.ForeignKey(WorkingMonth, on_delete=models.CASCADE,)
    full_time_employer_id = models.ForeignKey(FulltimeEmployer, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}-{}'.format(self.id, self.full_time_employer_id.employer_id.name)