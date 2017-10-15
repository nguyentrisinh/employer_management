from django.db import models

from .employer import Employer


class FulltimeEmployer(models.Model):
    objects = models.Manager()

    month_salary = models.DecimalField(max_digits=15, decimal_places=1)
    salary_level = models.FloatField()
    allowance = models.DecimalField(max_digits=15, decimal_places=1)

    employer_id = models.OneToOneField(Employer, unique=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.id, self.employer_id.id, self.employer_id.name)

