from Main.default_result import DefaultResult
from Main.validators import is_valid_html_color

from .models import TaskList
from Projects.models import Project


def get_task_lists(project_id: int = 0) -> DefaultResult:
    result = DefaultResult(data = {})
    
    try:
        project = Project.objects.get(id=project_id, deleted=False)
        task_lists = TaskList.objects.filter(project=project)
    except:
        return result
    for task_list in task_lists:
        result.data[str(task_list.id)] = task_list.__dict__

    result.success = 1
    result.message = "Success"

    return result


def validate_task_list(name: str = "", descr: str = "", color: str = "") -> list[str]:
    errors = []

    if not len(name.strip()):
        errors.append("Name is required")
    if len(name.strip()) > TaskList._meta.get_field("name").max_length:
        errors.append(f"Name must not exceed {TaskList._meta.get_field("name").max_length} characters")

    if len(color.strip()) and not is_valid_html_color(color):
        errors.append("Color is not a valid color")

    return errors


def modify_task_list(project_id: int = 0, task_list_id: int = 0, name: str = "", descr: str = "", color: str = "") -> DefaultResult:
    result = DefaultResult(data = {})
    result.errors = validate_task_list(name, descr, color)
    if len(result.errors):
        result.message = ""
        return result
    
    if project_id == 0:
        result.errors.append("Project ID is required")
        return result

    try:
        project = Project.objects.get(id=project_id, deleted=False)
    except:
        result.errors.append("Project not found")
        return result
    
    if int(task_list_id) != 0:
        try:
            task_list = TaskList.objects.get(id=task_list_id)
        except:
            result.errors.append("Task list not found")
            return result

        if not task_list:
            result.errors.append("Task list not found")
            return result
    else:
        task_list = TaskList()
    
    task_list.project = project
    task_list.color = color
    task_list.name = name
    
    task_list.save()
    result.success = 1
    result.message = "Success"

    return result


def find_tasks(task_list_id: int = 0) -> DefaultResult:
    result = DefaultResult(data = {})
    return result
