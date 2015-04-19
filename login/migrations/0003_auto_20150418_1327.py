# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150418_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurements',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='vesnareading',
            name='measurements',
        ),
        migrations.DeleteModel(
            name='Measurements',
        ),
        migrations.DeleteModel(
            name='VesnaReading',
        ),
    ]
