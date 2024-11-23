from enum import Enum
from Project.alarm import set_alarm
import csv

file_path = 'list.txt'

class Priority(Enum):
    high = 2
    mid = 1
    low = 0

class ToDo:
    def __init__(self, task=None, date=None, due_time=None, priority=None, is_done=None) -> None:
        self.task = task
        self.date = date
        self.due_time = due_time
        self.priority = priority
        self.is_done = is_done
    
    def set_task(self):
        self.task = input("Enter Task: ") #Take the task

        self.date = input("Enter Date: ") #take the date of the task
        
        priority_input = input("Enter priority (high, mid, low): ").strip().lower()
        priority_mapping = {
            'high': Priority.high,
            'mid': Priority.mid,
            'low': Priority.low
        }
        self.priority = priority_mapping.get(priority_input, Priority.low) #set the priority of the task

    def set_is_done(self):
        is_done_input = input(f'Is the task {self.task} done or no: ').strip().lower()
        if is_done_input == 'done':
            self.is_done = "good jop keep going"
        elif is_done_input == 'no':
            self.is_done = "Go do your tasks"
        else:
            self.is_done = "Invalid input"

    def print_to_do(self):
        print(f"{self.task} is due {self.date} and is {self.is_done}")

def main():
    tasks = []

    while True:
        action = input("Enter a command (add, show, quit): ").strip().lower()
        if action == 'add':
            task = ToDo()
            task.set_task()
            #task.set_is_done()
            tasks.append(task)
        elif action == 'show':
            for task in tasks:
                task.print_to_do()
        elif action == 'quit':
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()