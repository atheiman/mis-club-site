from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Member, Meeting, User
from .forms import RegisterForm



context_base = {}



def index(request):
    context = context_base

    return render(request, 'attendance/index.html', context)



def register(request):
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)

        if form.is_valid():

            # create a new user
            new_user = User.objects.create_user(username=form.cleaned_data['username'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            # redirect
            return HttpResponseRedirect(reverse('attendance:register'))

    else:
        form = RegisterForm()

    return render(request, 'attendance/register.html', {'form': form})



def signin(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)

    context = context_base

    return render(request, 'attendance/signin.html', context)
