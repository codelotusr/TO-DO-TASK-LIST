import os
import csv
import time
from pyllist import sllist
from collections import deque

task_path = os.getcwd() + "\\tasks.csv"
if not os.path.isfile(task_path):
    print("No task list found. Creating a new task list...")
    with open(task_path, "w", newline="") as task_file:
        writer = csv.writer(task_file)
        writer.writerow(["Task", "Subject", "Due Date", "Description"])
        print("Task list created.")
        input("Press enter to continue...")

deleted_task_path = os.getcwd() + "\\deleted_tasks.csv"
if not os.path.isfile(deleted_task_path):
    print("No deleted task list found. Creating a new deleted task list...")
    with open(deleted_task_path, "w", newline="") as deleted_task_file:
        writer = csv.writer(deleted_task_file)
        writer.writerow(["Task", "Subject", "Due Date", "Description"])
        print("Deleted task list created.")
        input("Press enter to continue...")

class Task:
    
    def __init__(self, task, subject, due_date, description):
        self.task = task
        self.subject = subject
        self.due_date = due_date
        self.description = description

    def __str__(self):
        return f"{self.task} - {self.subject} - {self.due_date} - {self.description}"

class Stack(deque):
    
    def push(self, item):
        self.append(item)
    
    def pop(self):
        return self.pop()
    
    def peek(self):
        return self[-1]
    
    def is_empty(self):
        return len(self) == 0
    
    def size(self):
        return len(self)
    
    def __str__(self):
        return str(self)

class TaskList(sllist):

    def __init__(self):
        super().__init__()
        self.load_tasks()

    def load_tasks(self):
        with open(task_path, "r", newline="") as task_file:
            print("Loading tasks...")
            reader = csv.reader(task_file)
            next(reader)
            for row in reader:
                self.append(Task(row[0], row[1], row[2], row[3]))

    def save_tasks(self):
        with open(task_path, "w", newline="") as task_file:
            writer = csv.writer(task_file)
            writer.writerow(["Task", "Subject", "Due Date", "Description"])
            for task in self:
                writer.writerow([task.task, task.subject, task.due_date, task.description])

    def display_tasks(self):
        print("Tasks:")
        for task in self:
            print (task)

    def add_task_start(self, task, subject, due_date, description):
        self.appendleft(Task(task, subject, due_date, description))
        self.save_tasks()
        print("Task added to the start of the list.")

    def add_task_end(self, task, subject, due_date, description):
        self.append(Task(task, subject, due_date, description))
        self.save_tasks()
        print("Task added to the end of the list.")

    def add_task_at(self, task, subject, due_date, description, index):
        at = self.nodeat(index - 1)
        self.insert(Task(task, subject, due_date, description), at)
        self.save_tasks()
        print("Task added at the index " + str(index) + ".")

    def remove_task_at(self, index):
        at = self.nodeat(index - 1)
        self.remove(at)
        self.save_tasks()
        print("Task removed at the index " + str(index) + ".")

    def remove_task_by_name(self, name):
        pass

def display_menu():
    print("Menu: [1] Display tasks, [2] Add task, [3] Delete task, [4] Undo, [5] Redo, [6] Exit\n")

task_list = TaskList()

while True:
    os.system("cls")
    display_menu()
    selection = int(input("Enter a number to select an option: "))
    if selection == 1:
        os.system("cls")
        task_list.display_tasks()
        input("Press enter to continue...")
    elif selection == 2:
        task_list.display_tasks()
        task = input("Enter the task: ")
        if task == "":
            task = "No task"
        subject = input("Enter the subject: ")
        if subject == "":
            subject = "No subject"
        due_date = input("Enter the due date (Year-Month-Day): ")
        due_date_in_seconds = time.mktime(time.strptime(due_date, "%Y-%m-%d"))
        if due_date_in_seconds < time.time():
            print("Invalid due date. The due date must be in the future.")
            input("Press enter to continue...")
            continue
        elif due_date == "":
            due_date = "No due date"
        description = input("Enter the description: ")
        if description == "":
            description = "No description"
        print("\nWhere do you want to add the task?\nAdd task: [1] Start, [2] End, [3] At")
        option = int(input("Enter a number to select an option: "))
        if option == 1:
            task_list.add_task_start(task, subject, due_date, description)
        elif option == 2:
            task_list.add_task_end(task, subject, due_date, description)
        elif option == 3:
            task_list.add_task_at(task, subject, due_date, description, int(input("Enter the index: ")))
        input("Press enter to continue...")
    elif selection == 3:
        task_list.display_tasks()
        print("Delete task: [1] By index, [2] By name")
        option = int(input("Enter a number to select an option: "))
        if option == 1:
            task_list.remove_task_at(int(input("Enter the index: ")))
        elif option == 2:
            task_list.remove_task_by_name(input("Enter the name: "))
        input("Press enter to continue...")
    elif selection == 6:
        break

input("Press enter to exit...")