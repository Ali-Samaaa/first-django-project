from django.urls import path
from . import views


urlpatterns = [
   path("", views.home_page),
   path("hello/", views.say_hello)
]