from django.urls import path
# from . import views
from .views import index, todo_list, todo_details

# Define the app name for namespacing
# This allows you to refer to this app's URLs in templates and other places
# using the format 'todo:index' for the index view.
# This is useful for avoiding name clashes with other apps in the project.
app_name = 'todo'  

urlpatterns = [
    path('index', index, name='todo-index'),
    path('todo_list', todo_list, name='todo-list'),
    path('todo_details/<int:task_id>', todo_details, name='todo-details'),
]