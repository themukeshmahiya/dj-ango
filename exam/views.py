from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def testpaper(request):
    p = "<h1>Testpaper from exam</h1>"
    return HttpResponse(p)

def result(request):
    r = "<h1>aagyo result tik k bath</h1>"
    return HttpResponse(r)

