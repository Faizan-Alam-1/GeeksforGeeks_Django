from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("This is about page")

def pk(request , pk):
    return HttpResponse(f"This pk {pk}")
