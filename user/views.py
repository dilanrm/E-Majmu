from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from .models import User
import json

def index(request):
    return HttpResponseRedirect('login')


def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
    form = AuthenticationForm()
    return render(request=request, template_name = 'main/login.html', context={'form':form})


def logout_req(request):
    logout(request)
    messages.info(request, "Log out sukses!")
    return redirect("main:homepage")


def regist(request):
    return HttpResponse('Hello')


def apiGetAll(request):
	users = (User.objects.all().values('name', 'username', 'password'))
	json_posts = json.dumps(list(users))
	return HttpResponse(json_posts, content_type='application/json')


def apiGetOne(request, uname):
	users = (Majmu.objects.filter(name=uname).values('name', 'username', 'password'))
	json_posts = json.dumps(list(users))
	return HttpResponse(json_posts, content_type='application/json')

