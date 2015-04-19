# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VesnaReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('CO', models.FloatField()),
                ('NO2', models.FloatField()),
                ('O3', models.FloatField()),
                ('humidity', models.FloatField()),
                ('movement', models.FloatField()),
                ('temp', models.FloatField()),
                ('readings', models.ForeignKey(to='login.Measurements')),
            ],
        ),
    ]
