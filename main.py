from PyQt6.QtWidgets import QComboBox,QTabWidget,QApplication,QLineEdit, QMainWindow,QHBoxLayout,QVBoxLayout , QVBoxLayout, QWidget, QCheckBox, QLabel, QPushButton, QStackedWidget, QMenuBar, QMessageBox
from PyQt6.QtCore import Qt

class project:
    def __init__(self, job, points):
        self.job = job
        self.points = points
        self.completed = False
    
    def complete(self):
        self.completed = True
    
    def uncomplete(self):
        self.completed = False

class bad_habit:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.completed = False
    
    def complete(self):
        self.completed = True
    
    def uncomplete(self):
        self.completed = False

class good_habit:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.completed = False
    
    def complete(self):
        self.completed = True
    
    def uncomplete(self):
        self.completed = False


class GUI:
    def __init__(self):
        self.point_count = 0
        self.projects = []
        self.bad_habits = []
        self.good_habits = []
        self.tabs = QTabWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    def setLayout(self, layout):
        self.layout = layout

    def add_project(self, job, points):
        self.projects.append(project(job, points))
    
    def add_bad_habit(self, name, points):
        self.bad_habits.append(bad_habit(name, points))
    
    def add_good_habit(self, name, points):
        self.good_habits.append(good_habit(name, points))
    
    def complete_project(self, index):
        self.projects[index].complete()
    
    def uncomplete_project(self, index):
        self.projects[index].uncomplete()
    
    def complete_bad_habit(self, index):
        self.bad_habits[index].complete()
    
    def uncomplete_bad_habit(self, index):
        self.bad_habits[index].uncomplete()
    
    def complete_good_habit(self, index):
        self.good_habits[index].complete()
    
    def uncomplete_good_habit(self, index):
        self.good_habits[index].uncomplete()
    
    def get_projects(self):
        return self.projects
    
    def get_bad_habits(self):
        return self.bad_habits
    
    def get_good_habits(self):
        return self.good_habits
    
    def create_main_tab(self):
        main_tab = QWidget()
        layout = QVBoxLayout(main_tab)

        # Display existing good habits
        layout.addWidget(QLabel("Good Habits"))
        for habit in self.good_habits:
            checkbox = QCheckBox(f"{habit.name} ({habit.points} points)")
            checkbox.stateChanged.connect(lambda state, h=habit: self.update_points(h, state))
            layout.addWidget(checkbox)

        # Display existing bad habits
        layout.addWidget(QLabel("Bad Habits"))
        for habit in self.bad_habits:
            checkbox = QCheckBox(f"{habit.name} ({habit.points} points)")
            checkbox.stateChanged.connect(lambda state, h=habit: self.update_points(h, state))
            layout.addWidget(checkbox)

        # Display existing projects
        layout.addWidget(QLabel("Projects"))
        for proj in self.projects:
            checkbox = QCheckBox(f"{proj.name} ({proj.points} points)")
            checkbox.stateChanged.connect(lambda state, p=proj: self.update_points(p, state))
            layout.addWidget(checkbox)

        # Input fields for adding new items
        input_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.points_input = QLineEdit()
        self.points_input.setPlaceholderText("Points")
        self.type_selector = QComboBox()
        self.type_selector.addItems(["Good Habit", "Bad Habit", "Project"])
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_new_item)

        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.points_input)
        input_layout.addWidget(self.type_selector)
        input_layout.addWidget(add_button)

        layout.addLayout(input_layout)
        main_tab.setLayout(layout)
        self.tabs.addTab(main_tab, "Main")

    def show(self):
        self.tabs.show()
    

    def update_points(self, item, state):
        if state == Qt.Checked:
            self.point_count += item.points
        else:
            self.point_count -= item.points
        print(f"Current Points: {self.point_count}")

    def add_new_item(self):
        name = self.name_input.text()
        points = int(self.points_input.text())
        item_type = self.type_selector.currentText()

        if item_type == "Good Habit":
            self.add_good_habit(name, points)
        elif item_type == "Bad Habit":
            self.add_bad_habit(name, points)
        elif item_type == "Project":
            self.add_project(name, points)

        self.create_main_tab()  # Refresh the tab to show the new item

if __name__ == "__main__":
    app = QApplication([])
    gui = GUI()
    gui.create_main_tab()
    gui.show()
    
