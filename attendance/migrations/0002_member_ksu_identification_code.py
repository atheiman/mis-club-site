# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ksu_identification_code',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
