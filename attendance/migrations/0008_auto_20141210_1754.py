# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20141206_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(help_text=b'ten digit phone number, xxx-xxx-xxxx', max_length=12, blank=True),
            preserve_default=True,
        ),
    ]
