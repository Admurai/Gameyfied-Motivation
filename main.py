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

        self.show_all_Items
        
    def add_projects (self, job, points):
        self.projects.append(project(job, points))
    def add_bad_habits (self, name, points):
        self.bad_habits.append(bad_habit(name, points))
    def add_good_habits (self, name, points):
        self.good_habits.append(good_habit(name, points))

    def show_all_Items(self):
        self.show_projects()
        self.show_bad_habits()
        self.show_good_habits()

    def show_projects(self):
        for project in self.projects:
            print(f"{project.job} - {project.points} - {project.completed}")
    
    def show_bad_habits(self):
        for bad_habit in self.bad_habits:
            print(f"{bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
    
    def show_good_habits(self):
        for good_habit in self.good_habits:
            print(f"{good_habit.name} - {good_habit.points} - {good_habit.completed}")

    def change(self):
        option = input("Would u like to complete any of these ? (y/n) ")
        if option == "y":
            self.complete()
        else:
            print("Ok")

    def complete(self):
        option = input("Which Type would u like to complete ? ")
        
        if option == "project":
            self.complete_project()
        elif option == "bad_habit":
            self.complete_bad_habit()
        elif option == "good_habit":
            self.complete_good_habit()
        else:
            print("Invalid Option")
    
    def complete_project(self):
        iteration = 1
        for project in self.projects:
            print(f"{iteration}:  {project.job} - {project.points} - {project.completed}")
            iteration+=1
        option = input("Which Project would u like to complete ?")
        self.projects[int(option)-1].complete()
        print("Project Completed")
    
    def complete_bad_habit(self):
        iteration = 1
        for bad_habit in self.bad_habits:
            print(f"{iteration}:  {bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
            iteration+=1
        option = input("Which Bad Habit would u like to complete ?")
        self.bad_habits[int(option)-1].complete()
        print("Bad Habit failed")
    
    def complete_good_habit(self):
        iteration = 1
        for good_habit in self.good_habits:
            print(f"{iteration}:  {good_habit.name} - {good_habit.points} - {good_habit.completed}")
            iteration+=1
        option = input("Which Good Habit would u like to complete ?")
        self.good_habits[int(option)-1].complete()
        print("Good Habit Completed")