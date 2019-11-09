from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
from intro.models import Contact

# Create your views here.

def index(requests):
    allcourses = Course.objects.all()
    catcourse = Course.objects.values('category')
    cats = {item['category'] for item in catcourse}
    cats = list(cats)
    print(cats.sort())
    category_by_course = []
    for cat in cats:
        cat_by_course = Course.objects.filter(category=cat)
        category_by_course.append(cat_by_course)
    print(category_by_course[0])
    params = {'allcourses': allcourses, 'cats': cats}
    return render(requests, 'intro/index.html', params)

def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        phno = requests.POST.get('phone')
        msg = requests.POST.get('message')
        contact = Contact(name=name, email=email, phone=phno, msg=msg)
        contact.save()
    return render(requests, 'intro/contact.html')
