from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que = "who developed python ?"
    a = "mk"
    b = "tk"
    c = "pk"
    d = "lk"

    context = {
         'Q': que,
         'options' : [ a,b,c,d ]
    }
    template = loader.get_template('testpaper.html')
    res = template.render(context,request)
    return HttpResponse(res)

def result(request):
    r = "<h1>aagyo result tik k bath</h1>"
    return HttpResponse(r)

