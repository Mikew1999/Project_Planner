from django.shortcuts import render
from django.http import HttpResponse

from Main.default_result import DefaultResult
from .task_list_manager import get_task_lists, modify_task_list
from .task_manager import find_tasks

# Create your views here.
def return_task_lists(request):
    result = DefaultResult(data = [])
    if request.method != "POST" or not request.user.is_authenticated:
        return HttpResponse(result.to_json(), content_type='application/json')

    project_id = request.POST.get('project_id', 0)
    task_lists = get_task_lists(project_id)

    for id in task_lists.data:
        result.data.append({
            "id": id,
            "name": task_lists.data[id]['name'],
            "colour": task_lists.data[id]['color'],
            "descr": task_lists.data[id]['descr'],
            "completion_perc": "0.00%"
        })

    result.success = 1
    result.message = "Success"

    return HttpResponse(result.to_json(), content_type='application/json')


def edit_task_list(request):
    result = DefaultResult()
    if request.method != "POST" or not request.user.is_authenticated:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    project_id = request.session.get('project_id', 0)
    if project_id == 0:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    task_list_id = request.POST.get('task_list_id', 0)
    name = request.POST.get('task_list_name', '')
    color = request.POST.get('task_list_colour', '')
    descr = request.POST.get('task_list_descr', '')

    result = modify_task_list(project_id, task_list_id, name, descr, color)

    return HttpResponse(result.to_json(), content_type='application/json')


def return_tasks(request):
    result = DefaultResult()
    if request.method != "POST" or not request.user.is_authenticated:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    project_id = request.session.get('project_id', 0)
    if project_id == 0:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    task_list_id = request.POST.get('task_list_id', 0)
    if task_list_id == "0":
        task_list_id = 0

    tasks = find_tasks(project_id, task_list_id)
    if not tasks.success:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    for id in tasks.data:
        result.data.append({
            "id": id,
            "name": tasks.data[id]['name'],
            "descr": tasks.data[id]['descr'],
            "status": tasks.data[id]['status_name'],
            "status_colour": tasks.data[id]['status_colour']
        })

    return HttpResponse(result.to_json(), content_type='application/json')
