from django.shortcuts import render, HttpResponse
from .models import *
from django.db import models
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
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
    return render(request,'meeting_app/meeting-details.html',context=dict)