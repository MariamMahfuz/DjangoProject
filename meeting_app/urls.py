from django.conf.urls import url
from django.urls import path
from meeting_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('meeting_details/',views.meeting_details,name='meeting-details'),
    path('meeting/',views.meeting,name='meeting')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
