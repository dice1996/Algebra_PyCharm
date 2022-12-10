

class TaskDto():
    
    def __init__(self):
        self.id = None
        self.text = None
        self.done = 0
        
    def __repr__(self):
        return f"TODO {self.id}: {self.text} - {self.done}"

    def add_task(self, text):
        new_task = TaskDto()
        new_task.text = text
        return new_task

    @staticmethod
    def map_data_from_database(entry: tuple):
        taskDto = TaskDto()
        taskDto.id = entry[0]
        taskDto.text = entry[1]
        taskDto.done = entry[2]

        return taskDto
