from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse("Welcome to Rugby fixtures")
def date(request):
    return HttpResponse("This page was served at "+ str(datetime.now()))
def about(request):
    return HttpResponse("Hello all rugby players. This page is used to know when and where you will have all your games and training. I hope you enjoy your use!")

