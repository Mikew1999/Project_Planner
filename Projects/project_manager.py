from .models import Status, Project, ProjectUser
from Main.default_result import DefaultResult
from Main.datatables import DataTable
from datetime import date


def get_user_projects(request, datatable: DataTable = None, id: int = 0):
    result = DefaultResult(data={})
    projects = Project.objects.filter(projectuser__user_id=request.user, deleted=False)
    if id != 0:
        projects = projects.filter(id=id)
        if not projects.exists():
            return result

    if datatable is not None:
        projects = projects[datatable.start : datatable.length]

    for project in projects:
        result.data[str(project.id)] = project.__dict__

    result.success = 1
    result.message = "Success"
    
    return result


def validate_project_details(request, name: str, descr: str, start_date: date, deadline: date, id: int) -> list[str]:
    errors = []
    dates_valid = True

    if id != 0:
        projects = get_user_projects(request, None, id)
        if not projects.success or id not in projects.data:
            return ["Access Denied"]
        
    if not len(name.strip()):
        errors.append("Project name is required")
    if len(name.strip()) > Project.name.max_length:
        errors.append("Project name must be less than " + Project.name.max_length)

    if len(descr.strip()) > Project.descr.max_length:
        errors.append("Project description must be less than " + Project.descr.max_length)


    if len(str(start_date).strip()) or not isinstance(start_date, date):
        errors.append("Start date is not a valid date")

    if len(str(deadline).strip()) or not isinstance(deadline, date):
        errors.append("Deadline is not a valid date")

    return errors


def edit_project(request, name: str, descr: str, start_date: date, deadline: date, id: int = 0) -> DefaultResult:
    result = DefaultResult()
    result.errors = validate_project_details(request, name, descr, start_date, deadline, id)
    if len(result.errors):
        result.message = ""
        return result
    
    if id == 0:
        status = Status.objects.get(name="Active")
        if not isinstance(start_date, date):
            start_date = None

        if not isinstance(deadline, date):
            deadline = None
        project = Project(name=name, descr=descr, start_date=start_date, deadline=deadline, owner=request.user, status=status)
        project.save()
        project_user = ProjectUser(user_id=request.user, project_id=project)
        project_user.save()
    else:
        project = Project.objects.get(id=id)
        project.name = name
        project.descr = descr
        project.start_date = start_date
        project.deadline = deadline
        project.save()

    result.success = 1
    result.message = "Success"
    return result


def delete_project(request, id: int) -> DefaultResult:
    try:
        project = Project.objects.get(id=id)
    except:
        pass
