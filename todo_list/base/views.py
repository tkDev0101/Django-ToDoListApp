# from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


#Login View
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    



class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm       #built in Form for registration
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
    






#View Taskss
class TaskList(LoginRequiredMixin, ListView): #task_list.html
    model = Task
    context_object_name = 'tasks'

    #User only sees their specific data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] =  context['tasks'].filter(user= self.request.user)
        context['count'] =  context['tasks'].filter(complete=False).count()
        return context
        


#Details of Task
class TaskDetail(LoginRequiredMixin, DetailView): #task.html
    model = Task
    context_object_name = 'task_title'
    template_name= 'base/task.html'
    

#Create Task
class TaskCreate(LoginRequiredMixin, CreateView): #task_form.html
    model = Task
    fields = {'title', 'description', 'complete'}
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    


#Update Task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = {'title', 'description', 'complete'}
    success_url = reverse_lazy('tasks')


#Delete Task
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
