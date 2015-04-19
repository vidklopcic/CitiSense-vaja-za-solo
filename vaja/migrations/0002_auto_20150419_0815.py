# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesnareading',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
