import json

class DefaultResult:
    def __init__(self, **kwargs):
        self.success = 0
        self.message = "Access Denied"
        self.errors = []

        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def to_json(self):
        return json.dumps(self.__dict__)
