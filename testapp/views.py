from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 
def greeting(request):
    s = "<h1>HEllo and WellCum of testapp</h1>"
    return HttpResponse(s)

def about(request):
    a = "<h1>About of testapp</h1>"
    return HttpResponse(a)

def contact(request):
    c = "<h1>contact of testapp</h1>"
    return HttpResponse(c)
