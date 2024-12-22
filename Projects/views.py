from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import date

from .models import *
from Main.datatables import DataTable
from Main.default_result import DefaultResult
from .statuses import get_statuses
from .project_manager import edit_project

@login_required
def index(request):
    statuses = get_statuses()
    for status in statuses.data:
        print(statuses.data[status])
    
    return render(request, "Projects/index.html")


def get_projects(request):
    # authorise user
    # validate csrf
    result = DefaultResult(data = [])
    if request.method != "POST":
        return HttpResponse(result.to_json(), content_type='application/json')

    # datatable = DataTable()

    projects = Project.objects.all().filter(deleted=False)[:10]

    for project in projects:
        result.data.append({
            "name": project.name,
            "completion_perc": "0.00%",
            "edit": ""
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
