from django.urls import path
from . import views


urlpatterns = [
   path("", views.home_page, name='home'),
   path("details/<int:todo_id>/", views.detail, name='details')
]