from django.shortcuts import render
from django.http import HttpResponse

from .models import Person

def persons(request):

    persons = Person.objects.all()
    context = {
        'persons': persons,
        'message': "Heelo this working"
    }

    return render(request, 'persons.html', context)