from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>virat scored century in wc semi finals<h1>')
def shreyas(request):
    return HttpResponse("<h1>shreyas scored century in wc semi finals<h1>")