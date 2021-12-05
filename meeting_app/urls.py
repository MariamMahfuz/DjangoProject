from django.conf.urls import url
from meeting_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('metting-etails/<int:pk>/',views.details_Meeting,name='dt-meeting'),

]

