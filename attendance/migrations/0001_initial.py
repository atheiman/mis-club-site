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
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(null=True, verbose_name=b'meeting date and time', blank=True)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('bonus', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=10, null=True, verbose_name=b'ten digit phone number, no symbols or spaces', blank=True)),
                ('year_in_school', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('major', models.CharField(default=b'MANAGEMENT INFORMATION SYSTEMS', max_length=40, choices=[(b'MANAGEMENT INFORMATION SYSTEMS', b'Management Information Systems'), (b'ACCOUNTING', b'Accounting'), (b'ENTREPRENEURSHIP', b'Entrepeneurship'), (b'FINANCE', b'Finance'), (b'MARKETING', b'Marketing'), (b'MANAGEMENT', b'Management'), (b'BUSINESS UNDECIDED', b'Business - Undecided'), (b'BUSINESS OTHER', b'Business - Other'), (b'NON BUSINESS', b'Non-Business')])),
                ('meetings', models.ManyToManyField(to='attendance.Meeting', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
