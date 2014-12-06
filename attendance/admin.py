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



def make_available_for_sign_in(modeladmin, request, queryset):
    queryset.update(available_for_sign_in=True)
make_available_for_sign_in.short_description = "Mark selected meetings as available for sign in"

def make_unavailable_for_sign_in(modeladmin, request, queryset):
    queryset.update(available_for_sign_in=False)
make_unavailable_for_sign_in.short_description = "Mark selected meetings as unavailable for sign in"

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
    actions = [make_available_for_sign_in, make_unavailable_for_sign_in]



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register MeetingAdmin
admin.site.register(Meeting, MeetingAdmin)
