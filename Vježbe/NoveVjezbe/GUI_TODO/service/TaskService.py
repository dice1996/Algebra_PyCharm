from utils.DBUtils import DBUtils
from datasource.dto.Task import TaskDto


class TaskService:
    TABLE_NAME = "task"

    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_table()

    def create_table(self):
        query = f'''
            create table if not exists {self.TABLE_NAME}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                done INTEGER NOT NULL            
            );        
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def add_task_to_table(self, task: TaskDto):
        query = f'''
            insert into {self.TABLE_NAME} (text, done)
            VALUES ("{task.text}", "{task.done}")        
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def retrieve_tasks(self):
        query = f'''
            select * from {self.TABLE_NAME} ORDER BY done;        
        '''
        output = DBUtils.db_fetch(self.sqlConnection, query)

        tasks = []
        for task in output:
            tasks.append(TaskDto.map_data_from_database(task))

        return tasks

    def retrieve_task(self, id):
        query = f'''
            select * from {self.TABLE_NAME} where id = {id};'''
        output = DBUtils.db_fetch(self.sqlConnection, query)
        task = TaskDto.map_data_from_database(output[0])
        return task

    def change_state(self, task: TaskDto):
        query = f'''
            update {self.TABLE_NAME}
            set done = 1
            where id = {task.id};'''

        DBUtils.db_execute(self.sqlConnection, query)
