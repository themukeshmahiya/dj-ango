from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    template = loader.get_template('testpaper.html')
    res = template.render()
    return HttpResponse(res)

def result(request):
    r = "<h1>aagyo result tik k bath</h1>"
    return HttpResponse(r)

