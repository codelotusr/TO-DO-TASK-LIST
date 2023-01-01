import os
import csv
import datetime
from pyllist import sllist, sllistnode
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
        print("Loading tasks...")
        self.load_tasks()
###
    def load_tasks(self):
        with open(task_path, "r", newline="") as task_file:
            reader = csv.reader(task_file)
            next(reader)
            for row in reader:
                self.append(Task(row[0], row[1], row[2], row[3]))
###
    def save_tasks(self):
        with open(task_path, "w", newline="") as task_file:
            writer = csv.writer(task_file)
            writer.writerow(["Task", "Subject", "Due Date", "Description"])
            for task in self:
                writer.writerow([task.task, task.subject, task.due_date, task.description])
###
    def display_tasks(self):
        i = 1
        print("Tasks:")
        for task in self:
            print (f"[{i}] {task}")
            i += 1
    def add_task_start(self, task, subject, due_date, description):
        self.appendleft(Task(task, subject, due_date, description))
        self.save_tasks()
        print("Task added to the start of the list.")
###
    def add_task_end(self, task, subject, due_date, description):
        self.append(Task(task, subject, due_date, description))
        self.save_tasks()
        print("Task added to the end of the list.")
###
    def add_task_at(self, task, subject, due_date, description, index):
        self.insert(Task(task, subject, due_date, description), self.nodeat(index - 1))
        self.save_tasks()
        print("Task added at the index " + str(index) + ".")
###
    def remove_task_at(self, index):
        self.remove(self.nodeat(index - 1))
        self.save_tasks()
        print("Task removed at the index " + str(index) + ".")
###
    def remove_task_by_name(self, name):
        task_count = 0
        for task in self:
            if task.task == name:
                task_count += 1
        if task_count == 0:
            print("No tasks with that name found.")
        elif task_count == 1:
            for index, task in enumerate(self):
                if task.task == name:
                    self.remove(self.nodeat(index))
                    self.save_tasks()
                    print("Task removed.")
        else:
            print("There are multiple tasks with the same name. Please use the index to remove the task.")
            index = int(input("Enter the index of the task to remove: "))
            self.remove_task_at(index)
###
    def search_by_due_date(self, due_date):
        os.system("cls")
        print("The following tasks are due on " + due_date + ":")
        for index, task in enumerate(self):
            if task.due_date == due_date:
                print(f"[{index + 1}] {task}")
    
    def search_by_subject(self, subject):
        os.system("cls")
        print("The following tasks are in the " + subject + " subject:")
        for index, task in enumerate(self):
            if task.subject == subject:
                print(f"[{index + 1}] {task}")
    
    def edit_task(self, index, choice, new_value):
        if choice == 1:
            self.nodeat(index - 1).value.task = new_value
        elif choice == 2:
            self.nodeat(index - 1).value.subject = new_value
        elif choice == 3:
            if len(new_value) != 10:
                print("Invalid date format. Please use YYYY-MM-DD.")
                print("Example: 2025-12-31")
                input("Press enter to return to menu...")
                return
            if datetime.datetime.strptime(new_value, "%Y-%m-%d") < datetime.datetime.now():
                print("Invalid date. Please enter a date that has not already passed.")
                return
            self.nodeat(index - 1).value.due_date = new_value
        elif choice == 4:
            self.nodeat(index - 1).value.description = new_value
        self.save_tasks()
        print("Task edited.")
    
    def save_deleted_tasks(self, task):
        with open(deleted_task_path, "w", newline="") as deleted_tasks_file:
            writer = csv.writer(deleted_tasks_file)
            writer.writerow(["Task", "Subject", "Due Date", "Description"])
            for task in self:
                writer.writerow([task.task, task.subject, task.due_date, task.description])

    def quicksort(self, start, end):
        if start < end:
            p = self.partition(start, end)
            self.quicksort(start, p - 1)
            self.quicksort(p + 1, end)

    def partition(self, start, end):
        pivot = self.nodeat(end).value.due_date
        i = start - 1
        for j in range(start, end):
            if self.nodeat(j).value.due_date <= pivot:
                i += 1
                self.swap(i, j)
        self.swap(i + 1, end)
        return i + 1
    
    def swap(self, i, j):
        temp = self.nodeat(i).value
        self.nodeat(i).value = self.nodeat(j).value
        self.nodeat(j).value = temp
    
    def sort_tasks(self):
        self.quicksort(0, len(self) - 1)
        self.save_tasks()
        print("Tasks sorted by due_date.")
    
    def remove_all_tasks(self):
        self.save_deleted_tasks(self)
        node = self.first
        next = node.next
        if node is not None:
            while next is not None:
                self.remove(node)
                node = next
                next = node.next
            self.remove(node)
        self.save_tasks()
        print("All tasks removed.")
    
    def undo(self):
        deleted_tasks = Stack()
        with open(deleted_task_path, "r", newline="") as task_file:
            reader = csv.reader(task_file)
            next(reader)
            for row in reader:
                deleted_tasks.push(Task(row[0], row[1], row[2], row[3]))
        with open(task_path, "w", newline="") as task_file:
            writer = csv.writer(task_file)
            writer.writerow(["Task", "Subject", "Due Date", "Description"])
            for task in deleted_tasks:
                writer.writerow([task.task, task.subject, task.due_date, task.description])
        self.load_tasks()
        self.save_tasks()
        print("Last action undone.")
    


def display_menu():
    print("Menu:[0] Help\n[1] Display tasks | [2] Add task | [3] Delete task | [4] Search for task | [5] Sort tasks | [6] Undo task clear | [7] Clear tasks | [8] Exit\n")

task_list = TaskList()

while True:
    os.system("cls")
    display_menu()
    selection = int(input("Enter a number to select an option: "))
    if selection == 0:
        print("[1] Display tasks: Displays all tasks in the list.")
        print("[2] Add task: Adds a task to the list.")
        print("[3] Delete task: Deletes a task from the list by index or by name.")
        print("[4] Search for task: Searches for a task by due date or subject and then gives you the option to edit the task.")
        print("[5] Sort tasks: Sorts the tasks by due date.")
        print("[6] Undo task clear: Undoes the last action that cleared the task list.")
        print("[7] Clear tasks: Clears all tasks from the list.")
        print("[8] Exit: Exits the program.")
        input("Press enter to return to menu...")
        
    elif selection == 1:
        os.system("cls")
        task_list.display_tasks()
        input("Press enter to return to menu...")
        
    elif selection == 2:
        task_list.display_tasks()
        task = input("Enter the task: ")
        if task == "":
            task = "No task"
        subject = input("Enter the subject: ")
        if subject == "":
            subject = "No subject"
        due_date = input("Enter the due date (Year-Month-Day): ")
        if len(due_date) != 10:
            print("Invalid date format. Please use YYYY-MM-DD.")
            print("Example: 2025-12-31")
            input("Press enter to return to menu...")
            continue
        if datetime.datetime.strptime(due_date, "%Y-%m-%d") < datetime.datetime.now():
            print("Invalid date. Please enter a date that has not already passed.")
            continue
        if due_date == "":
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
        input("Press enter to return to menu...")
        
    elif selection == 3:
        task_list.display_tasks()
        print("Delete task: [1] By index, [2] By name")
        option = int(input("Enter a number to select an option: "))
        if option == 1:
            task_list.remove_task_at(int(input("Enter the index: ")))
        elif option == 2:
            task_list.remove_task_by_name(input("Enter the name: "))
        input("Press enter to return to menu...")
        
    elif selection == 4:
        task_list.display_tasks()
        option = int(input("Search for task: [1] By due date, [2] By subject\nEnter a number to select an option: "))
        if option == 1:
            task_list.search_by_due_date(input("Enter the due date (Year-Month-Day): "))
        elif option == 2:
            task_list.search_by_subject(input("Enter the subject: "))
        print("\nEdit task: [1] Yes, [2] No")
        option = int(input("Enter a number to select an option: "))
        if option == 1:
            index = int(input("Enter the index of the task to edit: "))
            print("Edit task: [1] Task, [2] Subject, [3] Due date, [4] Description")
            option = int(input("Enter a number to select an option: "))
            task_list.edit_task(index, option, input("Enter the new value: "))
        if option == 2:
            pass
        input("Press enter to return to menu...")
        
    elif selection == 5:
        task_list.sort_tasks()
        input("Press enter to return to menu...")
    
    elif selection == 6:
        task_list.undo()
        input("Press enter to return to menu...")
    
    elif selection == 7:
        task_list.remove_all_tasks()
        input("Press enter to return to menu...")
    
    elif selection == 8:
        input("Goodbye! Press enter to exit...")
        break