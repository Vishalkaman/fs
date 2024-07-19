from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def ahead_time(req):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    res = "<h1>Ahead time is %s" %(dt)
    return HttpResponse(res)

def behind_time(req):
    dt = datetime.datetime.now() - datetime.timedelta(hours=4)
    res = "<h1>Ahead time is %s" %(dt)
    return HttpResponse(res)
