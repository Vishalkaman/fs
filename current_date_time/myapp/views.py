from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def cdt(req):
    date_time = datetime.datetime.now()
    res = "<h1>CDT is %s"%(date_time)
    return HttpResponse(res)
