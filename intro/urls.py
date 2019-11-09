from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home_Page"),
    path('intro/contact/', views.contact, name="Contact"),

]
