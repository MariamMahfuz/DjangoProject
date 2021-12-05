from django.conf.urls import url
from django.urls import path, include
from meeting_app import views

app_name='meeting_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('metting_details/<int:pk>/',views.details_Meeting,name='meeting_details'),
    path('froala_editor/', include('froala_editor.urls'))
]

