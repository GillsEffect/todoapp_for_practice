from django.contrib import admin
from django.urls import path, include
from . import views as Todo_views

app_name = 'todos'

urlpatterns = [
    path('new-todo/', Todo_views.create_todo, name ='new-todo'),
    path('todo_detail/<int:pk>', Todo_views.todo_detail, name ='todo_detail'),
    path('todo_edit/<int:pk>', Todo_views.todo_edit, name ='todo_edit'),
    path('update/<int:pk>', Todo_views.todo_update, name ='update'),
    path('delete/<int:pk>', Todo_views.todo_delete, name ='delete'),

]
