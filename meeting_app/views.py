from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def index(requst):
    cover = Cover.objects.all()
    service = Service.objects.all()
    upcoming = Up_Events.objects.all().order_by('id')

    heading = Heading.objects.all()

    dict = {'cover': cover, 'service': service, 'heading': heading,
            'upcoming': upcoming,
            }

    return render(requst, 'meeting_app/index.html', context=dict)


def details_Meeting(request, pk):
    mt_details = metting_details.objects.get(title_id=pk)
    print("test", mt_details)
    up_data = Up_Events.objects.get(id=pk)
    dict = {'mt_details': mt_details, 'up_data': up_data}
    return render(request, 'meeting_app/meeting-details.html', context=dict)
