from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Member, Meeting



context_base = {}



def index(request):
    context = context_base

    return render(request, 'attendance/index.html', context)



def meeting_list(request):
    context = context_base

    return render(request, 'attendance/meeting_list.html', context)



def signin(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)

    context = context_base

    return render(request, 'attendance/signin.html', context)
