from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ToDoModel
from django.urls import reverse_lazy


# Create your views here.


class TodoListView(ListView):
    template_name = 'todo/list.html'
    model = ToDoModel


class TodoDetailView(DetailView):
    template_name = 'todo/detail.html'
    model = ToDoModel


class TodoCreateView(CreateView):
    template_name = 'todo/create.html'
    model = ToDoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class TodoDeleteView(DeleteView):
    template_name = 'todo/delete.html'
    model = ToDoModel
    success_url = reverse_lazy('list')


class TodoUpdateView(UpdateView):
    template_name = 'todo/update.html'
    model = ToDoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
