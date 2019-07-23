from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return render(requests, 'courses/index.html')

def category(requests, category):
	return render(requests, 'courses/index.html')

def course(requests, category, cname):
    return render(requests, 'courses/course.html')

def tutorials(requests, category, cname):
    return render(requests, 'courses/tutorial.html')

def examples(requests, category, cname):
    return render(requests, 'courses/example.html')