from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def common():
    catcourse = Course.objects.values('category')
    cats = {item['category'] for item in catcourse}
    cats = list(cats)
    print(cats.sort())
    return cats

def index(requests):
    allcourses = Course.objects.all()
    cats = common()
    params = {'allcourses':allcourses, 'cats':cats}
    return render(requests, 'courses/index.html', params)

def category(requests, category):
    cat = Course.objects.filter(category=category)
    cats = common()
    params = {'allcourses':cat, 'cats':cats}
    return render(requests, 'courses/index.html', params)

def course(requests, category, cname):
    course = Course.objects.filter(course_name=cname)
    print(course)
    cats = common()
    parameter = {'cats':cats, 'course':course[0]}
    return render(requests, 'courses/course.html', parameter)

def tutorials(requests, category, cname):
    cats = common()
    return render(requests, 'courses/tutorial.html')

def examples(requests, category, cname):
    return render(requests, 'courses/example.html')