from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Majmu
import json

def index(request):
    majmus = Majmu.objects.all()
    return render(request, 'index.html')


def apiGetAll(request):
	majmus = (Majmu.objects.all().values('name', 'page', 'slug'))
	json_posts = json.dumps(list(majmus))
	return HttpResponse(json_posts, content_type='application/json')


def apiGetOne(request, majmu):
	majmus = (Majmu.objects.filter(slug=majmu).values('name', 'page', 'slug'))
	json_posts = json.dumps(list(majmus))
	return HttpResponse(json_posts, content_type='application/json')

