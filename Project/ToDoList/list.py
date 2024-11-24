import os

file_path = 'list.txt'

class ToDo:
    def __init__(self, task=None, date=None, due_time=None, priority='low', is_done=None):
        self.task = task
        self.date = date
        self.due_time = due_time
        self.priority = priority
        self.is_done = is_done

    def set_task(self):
        while True:
            self.task = input("Enter Task: ").strip()
            if '|' in self.task:
                print("Invalid character '|' in task. Please enter again.")
            else:
                break
        while True:
            self.date = input("Enter Date (YYYY-MM-DD): ").strip()
            if '|' in self.date:
                print("Invalid character '|' in date. Please enter again.")
            else:
                break
        while True:
            self.due_time = input("Enter Due Time (HH:MM): ").strip()
            if '|' in self.due_time:
                print("Invalid character '|' in due time. Please enter again.")
            else:
                break

    def set_priority(self):
        while True:
            self.priority = input("Enter priority (high, mid, low): ").strip().lower()
            if '|' in self.priority:
                print("Invalid character '|' in priority. Please enter again.")
            elif self.priority not in ['high', 'mid', 'low']:
                print("Invalid priority. Setting to 'low' by default.")
                self.priority = 'low'
                break
            else:
                break

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

    def print_to_do(self):
        status = "Done" if self.is_done else "Not Done"
        print(f"Task: {self.task}, Date: {self.date}, Due Time: {self.due_time}, Priority: {self.priority}, Status: {status}")

    def delete_task(self):
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\nCurrent Tasks:")

        idx = 1

        for task in tasks:
            print(f"{idx}. {task.task}")
            idx += 1
        try:
            task_number = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                selected_task = tasks.pop(task_number - 1)
                ToDo.save_tasks_to_txt(tasks)
                print(f"Task '{selected_task.task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def edit_task(self):
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\nCurrent Tasks:")

        idx = 1
        for task in tasks:
            print(f"{idx}. {task.task}")
            idx += 1

            task_number = int(input("\nEnter the number of the task to edit: "))
            if 1 <= task_number <= len(tasks):
                selected_task = tasks[task_number - 1]
                new_message = input("Enter the new message: ")
                if '|' in new_message:
                    print("Invalid character '|' in task. Please enter again.")
                    return
                selected_task.task = new_message.strip()
                ToDo.save_tasks_to_txt(tasks)
                print(f"Task '{selected_task.task}' edited successfully.")
            else:
                print("Invalid task number.")

def main():
    while True:

        action = input("Enter a command (add, show, edit, set, delete, quit): ").strip().lower()

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

        elif action =='edit':
            task = ToDo()
            task.edit_task()

        elif action == 'set':
            ToDo.set_is_done()

        elif action == 'delete':
            task = ToDo()
            task.delete_task()

        elif action == 'quit':
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()