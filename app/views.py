from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Person
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

    persons = Person.objects.all()
    context = {
        'persons': persons,
    }

    return render(request, 'persons.html', context)

@login_required
def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context = {
        'person': person,
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
        }
    return render(request, 'person_add_edit.html', context)