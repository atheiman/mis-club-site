# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20141205_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='available_for_sign_in',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=12, verbose_name=b'ten digit phone number, no symbols or spaces', blank=True),
            preserve_default=True,
        ),
    ]
