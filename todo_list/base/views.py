from django.http import HttpResponse
from django.shortcuts import render
from.models import Task


# Create your views here.
def taskList(request):
    return HttpResponse('To Do List')