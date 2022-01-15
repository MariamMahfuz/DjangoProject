from django.urls import path

from Login_App import views

urlpatterns = [
    path('register/', views.register_attempt, name='register_attempt'),
    path('login/',views.Login_attempt,name='login_attempt'),
]
