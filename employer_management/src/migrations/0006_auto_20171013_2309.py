# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_remove_fulltimesalary_working_day_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='employer_id',
        ),
    ]
