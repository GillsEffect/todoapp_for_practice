from django.shortcuts import render
from todos.models import Todo
# Create your views here.
def homepage(request):
    todos = Todo.objects.all().order_by('title')
    return render(request, 'homepage.html', {'todos': todos})
