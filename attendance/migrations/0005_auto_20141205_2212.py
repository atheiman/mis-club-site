# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20141205_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='description',
            field=models.TextField(default='default description', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='major',
            field=models.CharField(blank=True, max_length=40, choices=[(b'MANAGEMENT INFORMATION SYSTEMS', b'Management Information Systems'), (b'ACCOUNTING', b'Accounting'), (b'ENTREPRENEURSHIP', b'Entrepeneurship'), (b'FINANCE', b'Finance'), (b'MARKETING', b'Marketing'), (b'MANAGEMENT', b'Management'), (b'BUSINESS UNDECIDED', b'Business - Undecided'), (b'BUSINESS OTHER', b'Business - Other'), (b'NON BUSINESS', b'Non-Business')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default=11111111, max_length=10, verbose_name=b'ten digit phone number, no symbols or spaces', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='year_in_school',
            field=models.CharField(blank=True, max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')]),
            preserve_default=True,
        ),
    ]
