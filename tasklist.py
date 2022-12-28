import csv
import os
import time
from pyllist import sllist
from collections import deque

path = os.getcwd() + "\\tasks.csv"
if not(os.path.isfile(path)):
    print("No task list found. Creating a new tasklist...")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Subject", "Due Date", "Description"])
        print("Tasklist created.")






input("Press 'Enter' to continue...")
