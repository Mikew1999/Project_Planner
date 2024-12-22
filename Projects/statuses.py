from .models import Status
from Main.default_result import DefaultResult

def get_statuses():
    result = DefaultResult(data={})

    statuses = Status.objects.all()
    for status in statuses:
        result.data[status.id] = {'name': status.name, 'colour': status.color}

    result.success = 1
    result.message = "Success"
    return result
