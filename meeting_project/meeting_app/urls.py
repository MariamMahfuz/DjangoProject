from django.conf.urls import url
from meeting_app import views
from django.urls import path
from meeting_app.views import *

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('meeting_page/<int:pk>/',views.meeting_page,name='details_metting'),
    path('Employeeform/',views.Employeeform,name='employee_form'),
    path('contact/', Contact.as_view(), name='Contact')
=======
    path('meeting-page/<int:pk>/',views.meeting_page,name='details_metting'),

>>>>>>> 576376bb3d31eb534b0fa0b15fffc8d41787f914

]

