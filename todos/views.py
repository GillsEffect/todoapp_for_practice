from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            newTodo = Todo(title = title)
            newTodo.save()
        return redirect('/')
    else:
        return render(request, 'todos/new-todo.html')
# Create your views here.

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_edit.html', {'todo': todo})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('/')

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('/')
