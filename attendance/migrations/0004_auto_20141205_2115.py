# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20141203_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='ksu_identification_code',
            field=models.BigIntegerField(unique=True),
            preserve_default=True,
        ),
    ]
