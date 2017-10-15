from django.db import models

from .department import Department


class Employer(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField()

    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}-{}'.format(self.id, self.name)
