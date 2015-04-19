# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import time
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0003_auto_20150418_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.TextField()),
                ('created', models.FloatField(default=time.time)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
