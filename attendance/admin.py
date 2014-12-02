from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Member, Meeting



# Inline admin descriptor for Member model
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'



# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberInline, )



class MeetingAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'date_time',
        'bonus',
        'description',
    ]
    list_display = [
        'title',
        'date_time',
    ]
    ordering = ['-date_time']



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register MeetingAdmin
admin.site.register(Meeting, MeetingAdmin)
