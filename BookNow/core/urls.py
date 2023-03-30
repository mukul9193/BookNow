from django.urls import path, include
from core import views
from .views import *
from django.contrib.auth import views as auth_view

from .forms import LoginForm


urlpatterns = [
    path('index/', views.index_view, name="index"),
    # path('home/',views.home,name='home'),
    path('register/', RegisterationView.as_view(), name="register"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('home/', views.home_view, name="home"),
    path('logout/', views.user_logout, name="logout"),
    # path('check/', views.check_page, name="logout"),

    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('dashboard2/', views.dashboard_view2, name="dashboard2"),
    path('dashboard3/', views.dashboard_view3, name="dashboard3"),
    path('dashboard4/', views.dashboard_view4, name="dashboard4"),


    path('settime1/', views.SetTimeOne.as_view(), name="settime1"),
    # path('settime2/', views.SetTime2.as_view(), name="settime2"),
    # path('settime3/', views.SetTime3.as_view(), name="settime3"),
    # path('settime4/', views.SetTime4.as_view(), name="settime4"),

    path('all_events1/', views.all_events1, name="all_events1"),
    path('all_events2/', views.all_events2, name="all_events2"),
    path('all_events3/', views.all_events3, name="all_events3"),
    path('all_events4/', views.all_events4, name="all_events4"),

    path('calendar1/', views.calendar1, name='calendar1'),
    path('calendar2/', views.calendar2, name='calendar2'),
    path('calendar3/', views.calendar3, name='calendar3'),
    path('calendar4/', views.calendar4, name='calendar4'),

]
