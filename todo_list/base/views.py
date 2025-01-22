# from django.http import HttpResponse
from django.shortcuts import render
from.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskList(ListView): #task_list.html
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView): #task.html
    model = Task
    context_object_name = 'task_title'
    template_name= 'base/task.html'
    

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
