from django.shortcuts import render
from django.http import HttpResponse


def user_register(request):
    return HttpResponse('user registeration page.')