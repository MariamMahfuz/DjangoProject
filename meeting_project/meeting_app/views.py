<<<<<<< HEAD
=======
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from .models import *
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
>>>>>>> 576376bb3d31eb534b0fa0b15fffc8d41787f914
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import *

=======
from django.views.generic.edit import DeleteView
from django.views import View
from django.urls import reverse
>>>>>>> 576376bb3d31eb534b0fa0b15fffc8d41787f914

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


def meeting_page(request, pk):
<<<<<<< HEAD
    mt_details = metting_details.objects.get(title_id=pk)
    print("test", mt_details)
    up_data = Up_Events.objects.get(id=pk)
    dict = {'mt_details': mt_details, 'up_data': up_data}
    return render(request, 'meeting_app/meeting-details.html', context=dict)


def Employeeform(request):
    emp_dt = EmployeeForm.objects.all()
    state_dt = StateName.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        website = request.POST.get('website')
        hosting = request.POST.get('hosting')
        comment = request.POST.get('comment')

        emp_form_ins = EmployeeForm(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            zip=zip,
            website=website,
            hosting=hosting,
            comment=comment
        )
        emp_form_ins.save()

        empForm_ins = StateName(
            state=state
        )
        empForm_ins.save()

    dict = {'emp_dt': emp_dt, 'state_dt': state_dt}
    return render(request, 'meeting_app/employeeForm.html', context=dict)


class Contact(TemplateView):
    template_name = './meeting_app/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message = "From:" + email + "n/" " " + message

        mail = EmailMessage(subject, message, to=[settings.EMAIL_HOST_USER])
        mail.content_subtype = 'html'
        mail.send()
        return render(request, './meeting_app/index.html')
=======
    meeting = metting_details.objects.get(title_id=pk)
    print("test",meeting)
    
    up_data = Up_Events.objects.get(id=pk)
    dict = {'meeting': meeting, 'up_data': up_data}
    return render(request, 'meeting_app/meeting-details.html', context=dict)
>>>>>>> 576376bb3d31eb534b0fa0b15fffc8d41787f914
