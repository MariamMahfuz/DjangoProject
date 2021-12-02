from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(requst):
    cover=Cover.objects.all()
    service = Service.objects.all()
    upcoming = Upcoming.objects.all()
    course = Courses.objects.all()
    overview = Overview.objects.all()

    dict = {'cover':cover,'service':service,'upcoming':upcoming,'course':course,'overview':overview}
    return render(requst, 'meeting_app/index.html', context=dict)


def meeting_details(request):
    dict = {}
    return render(request, 'meeting_app/meeting-details.html', context=dict)


def meeting(request):
    dict = {}
    return render(request, 'meeting_app/meetings.html', context=dict)
