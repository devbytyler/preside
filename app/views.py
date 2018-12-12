import collections

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Prefetch, Max
# from django.core.validators import validate_email
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Person, Meeting
from app import forms

def sign_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            if user is not None:
                login(request, user)
                return redirect('persons')
    else:
        form = forms.LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required
def persons(request):
    SORT_BY_OPTIONS = collections.OrderedDict()
    SORT_BY_OPTIONS['first_name'] = 'First Name'
    SORT_BY_OPTIONS['last_name'] = 'Last Name'
    SORT_BY_OPTIONS['apartment'] = 'Apartment'
    SORT_BY_OPTIONS['status'] = 'Status'
    SORT_BY_OPTIONS['gender'] = 'Gender'
    SORT_BY_OPTIONS['meetings'] = 'Last meeting'

    sort_by = request.GET.get('sort_by') or 'first_name'

    latest_meeting_pks = Meeting.objects.all().values('person').annotate(max_id=Max('id')).values_list('max_id', flat=True)
    persons = Person.objects.prefetch_related(Prefetch(
        "meetings",
        queryset=Meeting.objects.filter(pk__in=latest_meeting_pks),
    )).filter(organization=request.user.organization)

    if sort_by == 'meetings':
        persons = sorted(list(persons), key=lambda x: x.meetings.first().id if x.meetings.first() else 0, reverse=True)
    else:
        persons = persons.order_by(sort_by)

    context = {
        'sort_by_options': SORT_BY_OPTIONS,
        'current_sort_name': SORT_BY_OPTIONS.get(sort_by) if sort_by else None,
        'persons': persons,
    }

    return render(request, 'persons.html', context)

@login_required
def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    status_options = Person.STATUS_OPTIONS
    meetings = Meeting.objects.filter(person=person).order_by("-id")
    if request.method == 'POST':
        form = forms.MeetingForm(request.POST, request=request,  instance=None)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.person = person
            meeting.user = request.user
            meeting.save()
            messages.success(request, 'Message saved successfull')
            return redirect('person', person.id)
    else:
        meeting_form = forms.MeetingForm(instance=None)
    context = {
        'meeting_form': meeting_form,
        'person': person,
        'status_options': status_options,
        'meetings': meetings
    }
    return render(request, 'person.html', context)


@login_required
def add_edit_person(request, person_id=None):
    person = get_object_or_404(Person, pk=person_id) if person_id else None
    context = {}
    if request.method == 'POST':
        form = forms.PersonForm(request.POST, request=request,  instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.organization = request.user.organization
            person.save()
            messages.success(request, 'Person saved successfully')
            return redirect('persons')
    else:
        form = forms.PersonForm(instance=person)
        context = {
            'form': form,
            'person': person
        }
    return render(request, 'person_add_edit.html', context)


@login_required
def update_status(request, person_id=None):
    person = get_object_or_404(Person, pk=person_id) if person_id else None
    if person:
        status = request.GET.get('s')
        person.status = status
        person.save()
    else:
        raise Http404
    return redirect('person', person.id)


@login_required
def meetings(request):
    meetings = Meeting.objects.filter(user__organization=request.user.organization)
    context = {
        'meetings': meetings,
    }

    return render(request, 'meetings.html', context)


@login_required
def delete_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id) if person_id else None
    person.delete()
    return redirect('persons')


# @login_required
# def add_edit_meeting(request, meeting_id):
#     meeting = get_object_or_404(Meeting, pk=meeting_id) if meeting_id else None
#     context = {}
#     if request.method == 'POST':
#         form = forms.MeetingForm(request.POST, request=request,  instance=meeting)
#         if form.is_valid():
#             meeting = form.save(commit=False)
#             meeting.organization = request.user.organization
#             meeting.save()
#             messages.success(request, 'Meeting saved successfully')
#             return redirect('meetings')
#     else:
#         form = forms.MeetingForm(instance=meeting)
#         context = {
#             'form': form,
#         }
#     return render(request, 'meeting_add_edit.html', context)

# @login_required
# def meeting(request, meeting_id):
#     meeting = get_object_or_404(Meeting, pk=meeting_id)
#     context = {
#         'meeting': meeting,
#     }
#     return render(request, 'meeting.html', context)