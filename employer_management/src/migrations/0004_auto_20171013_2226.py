# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_fulltimesalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='employer_id',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
