# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_member_ksu_identification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='meetings',
            field=models.ManyToManyField(related_name='members', null=True, to='attendance.Meeting', blank=True),
            preserve_default=True,
        ),
    ]
