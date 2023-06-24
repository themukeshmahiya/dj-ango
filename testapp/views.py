from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
 
def greeting(request):
    s = "<h1>HEllo and WellCum of testapp</h1>"
    return HttpResponse(s)

def about(request):
    template = loader.get_template('about.html')
    res = template.render()
    return HttpResponse(res)

def contact(request):
    c = "<h1>contact of testapp</h1>"
    return HttpResponse(c)
