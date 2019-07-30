from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import forms
from .models import Todo

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        newTodo = Todo(title = title, check = False)
        newTodo.save()
        return redirect('/')
    else:
        return render(request, 'todos/new-todo.html')
# Create your views here.

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_detail.html', {'todo': todo})
