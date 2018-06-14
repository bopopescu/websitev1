from django.shortcuts import render, HttpResponse
from .models import (Language, Lists, Articles)

def index(request):
    return HttpResponse('Hello From the Other Side')
