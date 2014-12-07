# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0006_auto_20141206_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='meetings',
        ),
        migrations.AddField(
            model_name='meeting',
            name='attendees',
            field=models.ManyToManyField(related_name='meetings', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=12, verbose_name=b'ten digit phone number, xxx-xxx-xxxx', blank=True),
            preserve_default=True,
        ),
    ]
