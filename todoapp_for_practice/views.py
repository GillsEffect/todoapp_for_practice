from django.shortcuts import render
from todos.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homepage(request):
    todos = Todo.objects.all().order_by('id')
    return render(request, 'homepage.html', {'todos': todos})
