from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
]
