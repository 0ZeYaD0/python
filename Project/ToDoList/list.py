from enum import Enum
import csv

file_path = 'list.txt'

class Priority(Enum):
    high = 2
    mid = 1
    low = 0

class ToDo:
    def __init__(self, task=None, date=None, priority=None, is_done=None) -> None:
        self.task = task
        self.date = date
        self.priority = priority
        self.is_done = is_done
    
    def set_task(self):
        self.task = input("Enter Task: ")


    def set_data(self):
        self.date = input("Enter Date: ")

    def set_priority(self):
        priority_input = input("Enter priority (high, mid, low): ").strip().lower()
        priority_mapping = {
            'high': Priority.high,
            'mid': Priority.mid,
            'low': Priority.low
        }
        self.priority = priority_mapping.get(priority_input, Priority.low)

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
    pass    

if __name__ == "__main__":
    main()