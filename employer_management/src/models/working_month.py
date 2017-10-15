from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class WorkingMonth(models.Model):
    objects = models.Manager()

    month = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    year = models.PositiveIntegerField()

    def __unicode__(self):
        return '{}/ {}-{}'.format(self.id, self.month, self.year)