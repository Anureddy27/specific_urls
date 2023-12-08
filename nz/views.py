from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def williamson(request):
    return HttpResponse('<h1> williamson scored 50 in wc semis')
def ravindra(request):
    return HttpResponse('<h1>young player<h1>')