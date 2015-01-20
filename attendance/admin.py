from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.urlresolvers import reverse

from .models import Member, Meeting, User



# Inline admin descriptor for Member model
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'



# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberInline, )



def meeting_link(obj):
    """
    Return a signin link to the meeting.
    """
    if not obj.available_for_sign_in:
        return "Not available for signin."
    url = reverse('attendance:signin', kwargs={'meeting_id':obj.id})
    return "<a href='{url}'>{text}</a>".format(text="Signin to this meeting",
                                                 url=url)
meeting_link.allow_tags = True
meeting_link.short_description = "Signin Link"

def make_available_for_sign_in(modeladmin, request, queryset):
    queryset.update(available_for_sign_in=True)
make_available_for_sign_in.short_description = "Mark selected meetings as available for sign in"

def make_unavailable_for_sign_in(modeladmin, request, queryset):
    queryset.update(available_for_sign_in=False)
make_unavailable_for_sign_in.short_description = "Mark selected meetings as unavailable for sign in"

class MeetingAdmin(admin.ModelAdmin):
    readonly_fields = [
        meeting_link,
        'id',
    ]
    fields = readonly_fields + [
        'title',
        'date_time',
        'bonus',
        'description',
        'attendees',
        'available_for_sign_in',
    ]
    list_display = [
        'id',
        meeting_link,
        'title',
        'date_time',
        'available_for_sign_in',
    ]
    ordering = ['-date_time']
    actions = [make_available_for_sign_in, make_unavailable_for_sign_in]



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register MeetingAdmin
admin.site.register(Meeting, MeetingAdmin)
