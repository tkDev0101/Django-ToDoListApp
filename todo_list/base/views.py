# from django.http import HttpResponse
from django.shortcuts import render
from.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class TaskList(ListView): #task_list.html
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView): #task.html
    model = Task
    context_object_name = 'task_title'
    template_name= 'base/task.html'
    