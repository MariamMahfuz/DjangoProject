from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def index(requst):
    dict = {}
    return render(requst, 'meeting_app/index.html', context=dict)


def meeting_details(request):
    dict = {}
    return render(request, 'meeting_app/meeting-details.html', context=dict)


def meeting(request):
    dict = {}
    return render(request, 'meeting_app/meeting.html', context=dict)
