from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Member, Meeting, User
from .forms import RegisterForm, SigninForm



context_base = {}



def index(request):
    context = context_base

    context['meetings'] = Meeting.objects.filter(available_for_sign_in=True)

    return render(request, 'attendance/index.html', context)



def register(request):
    context = context_base

    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)

        if form.is_valid():

            # create a new user
            new_user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            member = Member.objects.create(
                user = new_user,
                phone = form.cleaned_data['phone'],
                year_in_school = form.cleaned_data['year_in_school'],
                major = form.cleaned_data['major'],
                ksu_identification_code = form.cleaned_data['ksu_identification_code'],
            )
            member.save()

            if form.cleaned_data['sign_in_to_active_meetings']:
                meetings = Meeting.objects.filter(available_for_sign_in=True)
                print "---Sign User %s into current meetings %s---" % (new_user.username, meetings)

            # redirect
            return HttpResponseRedirect(
                reverse('attendance:register')+"?new_user=%s" % new_user.username
            )

    else:
        form = RegisterForm()

    context['form'] = form
    return render(request, 'attendance/register.html', context)



def signin(request, meeting_id):
    context = context_base

    meeting = get_object_or_404(Meeting, pk=meeting_id)
    if meeting.available_for_sign_in == False:
        return HttpResponse(
            "<strong>Error: Meeting (id = %d) not available for sign in.\
            Edit in <a href='/admin'>admin interface</a>.</strong>" % meeting.id,
            status_code=400,
        )

    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        form = SigninForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['ksu_identification_code'] != "":
                pass

            if form.cleaned_data['sign_in_to_active_meetings']:
                meetings = Meeting.objects.filter(available_for_sign_in=True)
                print "---Sign User %s into current meetings %s---" % (new_user.username, meetings)

            # redirect
            return HttpResponseRedirect(
                reverse('attendance:register')+"?new_user=%s" % new_user.username
            )

    else:
        form = SigninForm()

    context['meeting'] = meeting
    context['form'] = form

    return render(request, 'attendance/signin.html', context)
