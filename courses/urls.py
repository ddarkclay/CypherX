from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="Home_Page"),
    path('<str:category>', views.category, name="Category_Page"),
    path('<str:category>/<str:cname>', views.course, name="Course Page"),
    path('<str:category>/<str:cname>/tutorials', views.tutorials, name="Tutorial Page"),
    path('<str:category>/<str:cname>/examples', views.examples, name="Examples Page"),
]
