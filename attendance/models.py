from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

from .global_vars import YEAR_IN_SCHOOL_CHOICES, MAJOR_CHOICES



admin.site.site_header = "MIS Club Site Administration"
admin.site.site_title = "MIS Club Site Administration"
admin.site.index_title = "Home"



class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField('meeting date and time', blank=True, null=True)
    description = models.TextField(max_length=1000)
    bonus = models.BooleanField(default=False)

    available_for_sign_in = models.BooleanField(default=False)

    # many to many relationship with users
    attendees = models.ManyToManyField(User, blank=True, null=True, related_name='meetings')

    def __unicode__(self):
        return self.title



class Member(models.Model):
    # Member is an extension of the built-in Django User class.
    # The built-in User class already has fields:
        # username
        # password
        # email
        # first_name
        # last_name
    user = models.OneToOneField(User)
    phone = models.CharField(
        "ten digit phone number, xxx-xxx-xxxx",
        max_length=12,
        blank=True,
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        blank=True,
    )
    major = models.CharField(
        max_length=40,
        choices=MAJOR_CHOICES,
        blank=True,
    )
    ksu_identification_code = models.BigIntegerField(unique=True)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def attended_count(self):
        return self.meetings.count()

    def attendance_percentage(self):
        return "{0:.0f}%".format(float(self.attended_count()) / float(Meeting.objects.filter(bonus=False).count()) * 100)

    def __unicode__(self):
        return self.user.username
