from django.db import models


class Department(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.name
