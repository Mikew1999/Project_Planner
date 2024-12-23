from Main.default_result import DefaultResult
from .models import Task
from Projects.models import Project

def find_tasks(project_id: int = 0, task_list_id: int = 0, **filters) -> DefaultResult:
    result = DefaultResult(data = {})
    try:
        project = Project.objects.get(id=project_id, deleted=False)
    except:
        return result

    

    return result
