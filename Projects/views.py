from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import date

from .models import *
from Main.datatables import DataTable
from Main.default_result import DefaultResult
from .statuses import get_statuses
from .project_manager import edit_project, get_user_projects

@login_required
def index(request):
    statuses = get_statuses()
    for status in statuses.data:
        print(statuses.data[status])

    return render(request, "Projects/index.html")


def get_projects(request):
    result = DefaultResult(data = [])
    if request.method != "POST":
        return HttpResponse(result.to_json(), content_type='application/json')

    projects = get_user_projects(request, DataTable(0, 10))

    for id in projects.data:
        result.data.append({
            "id": id,
            "name": projects.data[id]['name'],
            "completion_perc": "0.00%",
            "edit": "<span class='del_project' style='cursor: pointer' title='Delete Project'><img height='25' width='25' src='/static/icons/delete_icon.png'></span>"
        })

    result.success = 1
    result.message = "Success"

    return HttpResponse(result.to_json(), content_type='application/json')


def edit_project_details(request):
    result = DefaultResult(project_id = 0)
    if request.method != "POST":
        return HttpResponse(result.to_json(), content_type='application/json')

    project_id = request.POST.get("project_id", 0)
    name = request.POST.get('name', '')
    descr = request.POST.get('descr', '')
    start_date = request.POST.get('start_date', date.today())
    deadline = request.POST.get('deadline', '')

    return HttpResponse(edit_project(request, name, descr, start_date, deadline, project_id).to_json(), content_type='application/json')


@login_required
def project(request):
    project_id = request.session.get('project_id', 0)
    if project_id == 0:
        return redirect('Projects:index')
    
    projects = get_user_projects(request, None, project_id)
    if projects.success != 1 or project_id not in projects.data:
        return redirect('Projects:index')

    return render(request, "Projects/project.html", {'project_info': projects.data[project_id]})


def set_project_in_session(request):
    result = DefaultResult()
    if request.method != "POST":
        result.message = "Invalid request"
        return HttpResponse(result.to_json(), content_type='application/json')
    
    project_id = request.POST.get('project_id', 0)
    if project_id == 0:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    projects = get_user_projects(request, None, project_id)
    if projects.success != 1 or project_id not in projects.data:
        return HttpResponse(result.to_json(), content_type='application/json')
    
    request.session['project_id'] = project_id
    result.success = 1
    result.message = "Success"

    return HttpResponse(result.to_json(), content_type='application/json')