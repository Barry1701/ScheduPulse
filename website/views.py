from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_website(request):
    return HttpResponse("Welcome To ScheduPulse!")