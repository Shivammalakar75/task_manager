

class Task:
    def __init__(self,task_id: int, title: str, description: str, status: str ="pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return self.__dict__
    

    
        