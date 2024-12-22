from .models import Status, Project, ProjectUser
from Main.default_result import DefaultResult
from datetime import date

def validate_project_details(name: str, descr: str, start_date: date, deadline: date) -> list[str]:
    errors = []
    return errors


def edit_project(request, name: str, descr: str, start_date: date, deadline: date, id: int = 0) -> DefaultResult:
    result = DefaultResult()
    result.errors = validate_project_details(name, descr, start_date, deadline)
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
