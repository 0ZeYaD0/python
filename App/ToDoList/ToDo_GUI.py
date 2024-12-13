import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QInputDialog, QMessageBox, QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from datetime import datetime
import os

file_path = 'list.txt'

class ToDo:
    def __init__(self, task=None, date=None, due_time=None, priority='low', is_done=None):
        self.task = task
        self.date = date
        self.due_time = due_time
        self.priority = priority
        self.is_done = is_done

    def append_task_to_file(self):
        with open(file_path, mode='a') as file:
            file.write(f"{self.task}|{self.date}|{self.due_time}|{self.priority}|{self.is_done}\n")

    @staticmethod
    def save_tasks_to_txt(tasks):
        priority_mapping = {'high': 1, 'mid': 2, 'low': 3}
        tasks_sorted = sorted(tasks, key=lambda task: priority_mapping[task.priority])
        with open(file_path, mode='w') as file:
            for task in tasks_sorted:
                file.write(f"{task.task}|{task.date}|{task.due_time}|{task.priority}|{task.is_done}\n")

    @staticmethod
    def load_tasks_from_txt():
        tasks = []
        if not os.path.exists(file_path):
            return tasks
        with open(file_path, mode='r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) != 5:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                task_str, date_str, due_time_str, priority, is_done_str = parts
                try:
                    is_done = is_done_str == 'True'
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    due_time = datetime.strptime(due_time_str, "%H:%M:%S").time()
                    tasks.append(ToDo(task_str, date, due_time, priority, is_done))
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()}\n{e}")
                    continue
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

        try:
            task_number = int(input("\nEnter the number of the task to edit: "))
            if 1 <= task_number <= len(tasks):
                selected_task = tasks[task_number - 1]
                new_message, ok = QInputDialog.getText(self, "Edit Task", "Enter the new message:")
                if ok and new_message:
                    selected_task.task = new_message
                    ToDo.save_tasks_to_txt(tasks)
                    QMessageBox.information(self, "Success", f"Task '{selected_task.task}' edited successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo for Everyone")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("D:/Down games/ToDo_Icon.png"))

        layout = QVBoxLayout()

        self.label = QLabel("Welcome to ToDo for Everyone", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.task_list_widget = QListWidget(self)
        layout.addWidget(self.task_list_widget)

        self.add_task_button = QPushButton("Add Task", self)
        self.add_task_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_button)

        self.show_tasks_button = QPushButton("Show Tasks", self)
        self.show_tasks_button.clicked.connect(self.show_tasks)
        layout.addWidget(self.show_tasks_button)

        self.set_done_button = QPushButton("Set Task as Done", self)
        self.set_done_button.clicked.connect(self.set_is_done)
        layout.addWidget(self.set_done_button)

        self.delete_task_button = QPushButton("Delete Task", self)
        self.delete_task_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_task_button)

        self.edit_task_button = QPushButton("Edit Task", self)
        self.edit_task_button.clicked.connect(self.edit_task)
        layout.addWidget(self.edit_task_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_tasks()

    def load_tasks(self):
        tasks = ToDo.load_tasks_from_txt()
        self.task_list_widget.clear()
        for task in tasks:
            item = QListWidgetItem(f"{task.task} - {task.date} - {task.due_time} - {task.priority} - {'Done' if task.is_done else 'Not Done'}")
            self.task_list_widget.addItem(item)

    def add_task(self):
        task, ok = QInputDialog.getText(self, "Add Task", "Enter Task:")
        if ok and task:
            date, ok = QInputDialog.getText(self, "Add Task", "Enter Date (YYYY-MM-DD):")
            if ok and date:
                due_time, ok = QInputDialog.getText(self, "Add Task", "Enter Due Time (HH:MM:SS):")
                if ok and due_time:
                    priority, ok = QInputDialog.getText(self, "Add Task", "Enter Priority (high, mid, low):")
                    if ok and priority:
                        new_task = ToDo(task, date, due_time, priority, False)
                        new_task.append_task_to_file()
                        QMessageBox.information(self, "Success", "Task added successfully!")
                        self.load_tasks()

    def show_tasks(self):
        tasks = ToDo.load_tasks_from_txt()
        if tasks:
            task_list = "\n".join([f"{idx + 1}. {task.task} - {task.date} - {task.due_time} - {task.priority} - {'Done' if task.is_done else 'Not Done'}" for idx, task in enumerate(tasks)])
            QMessageBox.information(self, "Task List", task_list)
        else:
            QMessageBox.information(self, "Task List", "No tasks found.")

    def set_is_done(self):
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            QMessageBox.information(self, "Set Task as Done", "No tasks found.")
            return

        task_number, ok = QInputDialog.getInt(self, "Set Task as Done", "Enter the number of the task to toggle its status:")
        if ok and 1 <= task_number <= len(tasks):
            selected_task = tasks[task_number - 1]
            selected_task.is_done = not selected_task.is_done
            ToDo.save_tasks_to_txt(tasks)
            QMessageBox.information(self, "Success", f"Task '{selected_task.task}' status updated successfully.")
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Invalid task number.")

    def delete_task(self):
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            QMessageBox.information(self, "Delete Task", "No tasks found.")
            return

        task_number, ok = QInputDialog.getInt(self, "Delete Task", "Enter the number of the task to delete:")
        if ok and 1 <= task_number <= len(tasks):
            selected_task = tasks.pop(task_number - 1)
            ToDo.save_tasks_to_txt(tasks)
            QMessageBox.information(self, "Success", f"Task '{selected_task.task}' deleted successfully.")
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Invalid task number.")

    def edit_task(self):
        tasks = ToDo.load_tasks_from_txt()
        if not tasks:
            QMessageBox.information(self, "Edit Task", "No tasks found.")
            return

        task_number, ok = QInputDialog.getInt(self, "Edit Task", "Enter the number of the task to edit:")
        if ok and 1 <= task_number <= len(tasks):
            selected_task = tasks[task_number - 1]
            new_message, ok = QInputDialog.getText(self, "Edit Task", "Enter the new message:")
            if ok and new_message:
                selected_task.task = new_message
                ToDo.save_tasks_to_txt(tasks)
                QMessageBox.information(self, "Success", f"Task '{selected_task.task}' edited successfully.")
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Invalid task number.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())