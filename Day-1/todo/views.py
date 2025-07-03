from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    # render(request,template_name,context=None,content_type=None)
    # redirect('/profile, permanent=False, *args, **kwargs)
    # res = HttpResponse("Hello, world!")
    # return res
    return render(request, 'main/base_layout.html')

task_list = [
    {'index': 0, 'id': 1, 'title': 'Task 1', 'description': 'Description for Task 1', 'priority': 1},
    {'index': 1, 'id': 2, 'title': 'Task 2', 'description': 'Description for Task 2', 'priority': 2},
    {'index': 2, 'id': 3, 'title': 'Task 3', 'description': 'Description for Task 3', 'priority': 3},
]

def todo_list(request):
    my_context = {
        'title': 'Todo List',
        'description': 'This is a list of tasks to be completed.',
        'tasks_list': task_list,
    }
    return render(request, 'todo/todo_list.html', context=my_context)

def todo_details(request, *args, **kwargs):
    task_id = kwargs.get('task_id')
    task_obj = _get_task_by_id(task_id)
    my_context = {
        'task_id': task_obj.get('id'),
        'task_title': task_obj.get('title'),
        'task_description': task_obj.get('description'),
        'task_priority': task_obj.get('priority'),
    }
    # for task in task_list:
    #     if task['id'] == task_id:
    #         my_context['task_id'] = task_id
    #         my_context['name'] = task['name']
    #         my_context['description'] = task['description']
    #         my_context['priority'] = task['priority']
    #         break
    
    # if not task:
    #     return HttpResponse("Task not found", status=404)
    
    # my_context = {
    #     'title': f"Task {task_id} Details",
    #     'task': task,
    # }
    
    return render(request, 'todo/todo_details.html', context=my_context)

def _get_task_by_id(task_id):
    for task in task_list:
        if 'id' in task and task['id'] == task_id:
            return task
    return None

def todo_update(request, *args, **kwargs):
    task_id = kwargs.get('task_id')
    task_obj = _get_task_by_id(task_id)

    for task in task_list:
        if task['id'] == task_id:
            # Here you would typically update the task with new data from the request.
            # For example, you might get data from request.POST or request.GET.
            # task['title'] = request.POST.get('title', task['title'])
            # task['description'] = request.POST.get('description', task['description'])
            # task['priority'] = request.POST.get('priority', task['priority'])
            break
    
    # if not task_obj:
    #     return HttpResponse("Task not found", status=404)
    
    # Here you would typically handle the update logic, e.g., updating the task in a database.
    # For now, we will just return a success message.
    
    return JsonResponse({'status': 'success', 'message': f'Task {task_id} updated successfully.'})