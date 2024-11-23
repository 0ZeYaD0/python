import os

file_path = 'tasks.txt'

class ToDo:
    def __init__(self, task=None, date=None, due_time=None, priority='low', is_done=None):
        self.task = task
        self.date = date
        self.due_time = due_time
        self.priority = priority
        self.is_done = is_done

    def set_task(self):
        self.task = input("Enter Task: ")
        self.date = input("Enter Date (YYYY-MM-DD): ")
        self.due_time = input("Enter Due Time (HH:MM): ")

    def set_priority(self):
        self.priority = input("Enter priority (high, mid, low): ").strip().lower()
        if self.priority not in ['high', 'mid', 'low']:
            print("Invalid priority. Setting to 'low' by default.")
            self.priority = 'low'

    def set_is_done(self):
        is_done_input = input(f'Is the task "{self.task}" done? (yes/no): ').strip().lower()
        self.is_done = is_done_input == 'yes'

    def save_to_txt(self):
        with open(file_path, mode='a') as file:
            file.write(f"{self.task}|{self.date}|{self.due_time}|{self.priority}|{self.is_done}\n")

    @staticmethod
    def save_tasks_to_txt(tasks):
        with open(file_path, mode='w') as file:
            for task in tasks:
                file.write(f"{task.task}|{task.date}|{task.due_time}|{task.priority}|{task.is_done}\n")

    @staticmethod
    def load_tasks_from_txt():
        tasks = []
        if not os.path.exists(file_path):
            return tasks
        with open(file_path, mode='r') as file:
            for line in file:
                task, date, due_time, priority, is_done_str = line.strip().split('|')
                is_done = is_done_str == 'True'
                tasks.append(ToDo(task, date, due_time, priority, is_done))
        return tasks

    def print_to_do(self):
        status = "Done" if self.is_done else "Not Done"
        print(f"Task: {self.task}, Date: {self.date}, Due Time: {self.due_time}, Priority: {self.priority}, Status: {status}")

    @staticmethod
    def set_is_done():
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\nCurrent Tasks:")
        idx = 1
        for task in tasks:
            status = "Done" if task.is_done else "Not Done"
            print(f"{idx}. {task.task} - {status}")
            idx += 1
        try:
            task_number = int(input("\nEnter the number of the task to toggle its status: "))
            if 1 <= task_number <= len(tasks):
                selected_task = tasks[task_number - 1]
                selected_task.is_done = not selected_task.is_done
                ToDo.save_tasks_to_txt(tasks)
                print(f"Task '{selected_task.task}' status updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        action = input("\nEnter a command (add, show, set, quit): ").strip().lower()
        if action == 'add':
            task = ToDo()
            task.set_task()
            task.set_priority()
            task.is_done = False
            task.save_to_txt()
            print("Task added successfully.")
        elif action == 'show':
            tasks = ToDo.load_tasks_from_txt()
            if tasks:
                print("\nTask List:")
                idx = 1
                for task in tasks:
                    print(f"{idx}. ", end="")
                    task.print_to_do()
                    idx += 1
            else:
                print("No tasks found.")
        elif action == 'set':
            ToDo.set_is_done()
        elif action == 'quit':
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()