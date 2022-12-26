import sqlite3
from tkinter import Frame
import tkinter as tk
from tkinter import ttk
from service.TaskService import TaskService
from datasource.dto.Task import TaskDto

DB_NAME = "todo.db"


class FirstScreen(Frame):
    def __init__(self, mainWindow):
        self.sqlConnection = sqlite3.connect(DB_NAME)
        TaskService(self.sqlConnection).create_table()
        super().__init__(mainWindow)
        self.grid()
        self.first_widget_group()

    def first_widget_group(self):
        self.window1 = tk.LabelFrame(self, text="TODO LISTA")
        self.window1.grid(row=0, column=0, padx=5, pady=5, columnspan=10, sticky="ew")
        self.show_tasks()
        label_text = ttk.Label(self.window1, text="Use 'Double-click' to mark selected task with 'Done'!")
        label_text.grid(row=2, column=0, padx=5, pady=5)
        self.todo_variable = tk.StringVar()
        self.todo_input = ttk.Entry(self.window1, textvariable=self.todo_variable, width=120)
        self.todo_input.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.todo_input.bind("<Return>", self.add_task)

    def double_click(self, event):
        item = self.task_list.selection()[0]
        id = self.task_list.item(item, "text")
        task = TaskService(self.sqlConnection).retrieve_task(id)
        TaskService(self.sqlConnection).change_state(task)
        self.show_tasks()

    def add_task(self, event):
        task = TaskDto().add_task(self.todo_variable.get())
        TaskService(self.sqlConnection).add_task_to_table(task)
        self.todo_variable.set("")
        self.show_tasks()

    def show_tasks(self):
        tasks = TaskService(self.sqlConnection).retrieve_tasks()
        self.task_list = ttk.Treeview(self.window1, columns=["id", "text", "done"], show='headings', height=20)
        self.task_list.column("# 1", anchor="center", width=3)
        self.task_list.column("# 3", anchor="center", width=12)
        self.task_list.heading('id', text="ID")
        self.task_list.heading('text', text="TASK")
        self.task_list.heading('done', text="DONE")

        for task in tasks:
            if task.done == 0:
                self.task_list.insert('', 'end', text=task.id, values=[task.id, task.text, "U PROCESU"])
            elif task.done == 1:
                self.task_list.insert('', 'end', text=task.id, values=[task.id, task.text, "RIJEŠENO"])

        self.task_list.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.task_list.bind("<Double-1>", self.double_click)
