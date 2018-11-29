from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': "Heelo this working"
    }

    return render(request, 'base.html', context)