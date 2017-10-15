from django.db import models

from .employer import Employer


class ParttimeEmployer(models.Model):
    objects = models.Manager()

    day_salary = models.DecimalField(max_digits=15, decimal_places=1)

    employer_id = models.OneToOneField(Employer, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.id, self.employer_id.id, self.employer_id.name)
