from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests, 'index.html')