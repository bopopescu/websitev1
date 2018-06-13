from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello From the Other Side')
