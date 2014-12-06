from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

from .global_vars import *



admin.site.site_header = "MIS Club Site Administration"
admin.site.site_title = "MIS Club Site Administration"
admin.site.index_title = "Home"



class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField('meeting date and time', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    bonus = models.BooleanField(default=False)

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
        "ten digit phone number, no symbols or spaces",
        max_length=10,
        blank=True,
        null=True,
    )
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    MAJOR_CHOICES = (
        (MANAGEMENT_INFORMATION_SYSTEMS, 'Management Information Systems'),
        (ACCOUNTING, 'Accounting'),
        (ENTREPRENEURSHIP, 'Entrepeneurship'),
        (FINANCE, 'Finance'),
        (MARKETING, 'Marketing'),
        (MANAGEMENT, 'Management'),
        (BUSINESS_UNDECIDED, 'Business - Undecided'),
        (BUSINESS_OTHER, 'Business - Other'),
        (NON_BUSINESS, 'Non-Business'),
    )
    major = models.CharField(
        max_length=40,
        choices=MAJOR_CHOICES,
        default=MANAGEMENT_INFORMATION_SYSTEMS,
    )
    ksu_identification_code = models.BigIntegerField()

    # There is no need to define a 'simple' many-to-many class in Django modeling.
    meetings = models.ManyToManyField(Meeting, blank=True, null=True, related_name='members')

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def attended_count(self):
        return self.meetings.count()

    def attendance_percentage(self):
        return "{0:.0f}%".format(float(self.attended_count()) / float(Meeting.objects.filter(bonus=False).count()) * 100)

    def __unicode__(self):
        return self.user.username

    # >>> from attendance.models import *
    # >>> user = User.objects.get(username='atheiman')
    # >>> user
    # <User: atheiman>
    # >>> member = user.member
    # >>> member
    # <Member: atheiman>
