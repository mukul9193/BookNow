from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from datetime import datetime
from django.db.models import Q

# def home(request):
#     return render(request,'myapp/home.html')


# def check_page(request):
#     return render(request, 'core/check.html')


def index_view(request):
    return render(request, 'core/index.html')


def dashboard_view(request):
    return render(request, 'core/dashboard.html')


def dashboard_view2(request):
    return render(request, 'core/dashboard2.html')


def dashboard_view3(request):
    return render(request, 'core/dashboard3.html')


def dashboard_view4(request):
    return render(request, 'core/dashboard4.html')


class RegisterationView(View):
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'core/signup.html', {'form': fm})

    def post(self, request):
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            messages.success(
                request, 'Congratulations || Registered Successfully')
            fm.save()
            fm = RegistrationForm()
        return render(request, 'core/signup.html', {'form': fm})


class UserLogin(View):
    def get(self, request):
        fm = LoginForm()
        return render(request, 'core/login.html', {'form': fm})

    def post(self, request):
        fm = LoginForm(request=request, data=request.POST)
        print("Hello Outside")
        if fm.is_valid():
            print("hello Inside")
            uname = fm.cleaned_data['username']
            print(uname)
            upass = fm.cleaned_data['password']
            print(upass)
            user = authenticate(username=uname, password=upass)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
        fm = LoginForm()
        return render(request, 'core/login.html', {'form': fm})


def home_view(request):
    return render(request, 'core/home.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')


# TODO---Event1--------------------------------------------------------------------------------------------------------

class SetTimeOne(View):
    def get(self, request):
        return render(request, 'core/settime1.html')

    def post(self, request):
        payload = request.POST
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        title = payload.get('title')
        name = payload.get('name')
        start_date = payload.get('start_date')
        end_date = payload.get('end_date')
        print(start_date)
        print(type(start_date))
        # TODO --> FOR TODAY DATE
        today_date = datetime.today()
        str_year = today_date.strftime("%Y")
        str_month = today_date.strftime("%m")
        str_date = today_date.strftime("%d")
        str_hour = today_date.strftime("%H")
        str_minute = today_date.strftime("%M")
        # TODO --> FOR USER_INPUT dATE AND tIME for starting date
        user_year = start_date[2:4]
        user_month = start_date[5:7]
        user_date = start_date[8:10]
        user_hour = start_date[11:13]
        user_min = start_date[14:16]
        # TODO --> FOR USER_INPUT dATE AND tIME for ending date
        user_year_end = end_date[2:4]
        user_month_end = end_date[5:7]
        user_date_end = end_date[8:10]
        user_hour_end = end_date[11:13]
        user_min_end = end_date[14:16]
        # TODO--> FOR CHECKING

        # TODO--> Conditions
        user_start_time = user_year+"/"+user_month + \
            "/"+user_date+" "+user_hour+":"+user_min
        format_data = "%y/%m/%d %H:%M"
        user_start_time_compiled = datetime.strptime(
            user_start_time, format_data)
        print("After comiled start----", user_start_time_compiled)
        print(type(user_start_time_compiled))

        user_end_time = user_year_end+"/"+user_month_end+"/" + \
            user_date_end+" "+user_hour_end+":"+user_min_end
        user_end_time_compiled = datetime.strptime(
            user_end_time, format_data)
        print("After compiled end", user_end_time_compiled)
        print(type(user_end_time_compiled))


        if (user_start_time_compiled >= today_date and user_end_time_compiled >= today_date):
            user_start_time = user_year+"/"+user_month + \
                "/"+user_date+" "+user_hour+":"+user_min
            format_data = "%y/%m/%d %H:%M"
            user_start_time_compiled = datetime.strptime(
                user_start_time, format_data)
            print("After comiled start----", user_start_time_compiled)
            print(type(user_start_time_compiled))
            # TODO---------------------------------------------------------------------------------

            user_end_time = user_year_end+"/"+user_month_end+"/" + \
                user_date_end+" "+user_hour_end+":"+user_min_end
            user_end_time_compiled = datetime.strptime(
                user_end_time, format_data)
            print("After compiled end", user_end_time_compiled)
            print(type(user_end_time_compiled))

            obj = MeetingRoom1.objects.filter(
                start__lt=user_start_time_compiled) and MeetingRoom1.objects.filter(end__gt=user_end_time_compiled)
            print("Finally", obj)
            if not obj:
                register = MeetingRoom1(
                    title=title, name=name, start=start_date, end=end_date)
                register.save()
                messages.success(
                    request, "Congratulation your Meeting scheduled successfully ")
                return redirect("dashboard")
            else:
                error_message = "Already Booked"
            return render(request, 'core/dashboard.html', {"error": error_message})
        else:
            error_message = "selected date should not be past "
            return render(request, 'core/dashboard.html', {"error": error_message})


def calendar1(request):
    context = {
        "events": all_events1
    }
    return render(request, 'core/calendar.html', context)


def all_events1(request):
    all_events = MeetingRoom1.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name+"("+event.title +")",
            # 'name': event.name,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S")
        })

    return JsonResponse(out, safe=False)

# TODO---Event-2--------------------------------------------------------------------------------------------------------


class SetTime2(View):
    def get(self, request):
        return render(request, 'core/settime2.html')

    def post(self, request):
        post_data = request.POST
        name = post_data.get('name')
        start = post_data.get('start')
        end = post_data.get('end')
        register = Event2(name=name, start=start, end=end)
        register.save()
        return redirect('dashboard2')


def calendar2(request):
    context = {
        "events": all_events2
    }
    return render(request, 'core/calendar2.html', context)


def all_events2(request):
    print("enter")
    all_events = Event2.objects.all()
    out = []
    for event in all_events:
        out.append({
            'name': event.name,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S")
        })
        print(out)

    return JsonResponse(out, safe=False)

# TODO---Event-3---------------------------------------------------------------------------------------------------------


class SetTime3(View):
    def get(self, request):
        return render(request, 'core/settime3.html')

    def post(self, request):
        post_data = request.POST
        name = post_data.get('name')
        start = post_data.get('start')
        end = post_data.get('end')
        register = Event3(name=name, start=start, end=end)
        register.save()
        return redirect('dashboard3')


def calendar3(request):
    context = {
        "events": all_events3
    }
    return render(request, 'core/calendar3.html', context)


def all_events3(request):
    print("enter")
    all_events = Event3.objects.all()
    out = []
    for event in all_events:
        out.append({
            'name': event.name,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S")
        })
        print(out)

    return JsonResponse(out, safe=False)

# TODO---Event-4--------------------------------------------------------------------------------------------------------


class SetTime4(View):
    def get(self, request):
        return render(request, 'core/settime4.html')

    def post(self, request):
        post_data = request.POST
        name = post_data.get('name')
        start = post_data.get('start')
        end = post_data.get('end')
        register = Event4(name=name, start=start, end=end)
        register.save()
        return redirect('dashboard4')


def calendar4(request):
    context = {
        "events": all_events4
    }
    return render(request, 'core/calendar4.html', context)


def all_events4(request):
    print("enter")
    all_events = Event4.objects.all()
    out = []
    for event in all_events:
        out.append({
            'name': event.name,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S")
        })
        print(out)

    return JsonResponse(out, safe=False)
