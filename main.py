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

        self.change
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
            option =input ("would u like to add any ? (y/n)")
            if option == "y":
                self.add()
            else:
                option =input("Would u like to remove any ?(y/n)")
                if option == "y":
                    self.remove()
                else:
                    option= input("Would u like to see your points ? (y/n)") 
                    if option == "y":
                        self.show_points()
                    else:
                        option = input("would u like to close the program ? (y/n)")
                        if option == "y":
                            print("Goodbye")
                            #save the data
                        else:
                                self.change()
    
        
    def complete(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit ?")
        
        if option == "1":
            self.complete_project()
        elif option == "2":
            self.complete_bad_habit()
        elif option == "3":
            self.complete_good_habit()
        else:
            print("please enter a number between 1 and 3")
            self.complete()
    
    def complete_project(self):
        iteration = 1
        for project in self.projects:
            print(f"{iteration}:  {project.job} - {project.points} - {project.completed}")
            iteration+=1
        option = input("Which Project would u like to complete ?")
        self.point_count += self.projects[int(option)-1].points
        self.projects[int(option)-1].complete()
        print("Project Completed")
    def complete_bad_habit(self):
        iteration = 1
        for bad_habit in self.bad_habits:
            print(f"{iteration}:  {bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
            iteration+=1
        option = input("Which Bad Habit would u like to complete ?")
        self.point_count
        self.bad_habits[int(option)-1].complete()
        print("Bad Habit failed") 
    def complete_good_habit(self):

        iteration = 1
        for good_habit in self.good_habits:
            print(f"{iteration}:  {good_habit.name} - {good_habit.points} - {good_habit.completed}")
            iteration+=1
        option = input("Which Good Habit would u like to complete ?")
        self.point_count += self.good_habits[int(option)-1].points
        self.good_habits[int(option)-1].complete()
        print("Good Habit Completed")

    def add(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit ?")
        if option == "1":
            self.add_project()
        elif option == "2":
            self.add_bad_habit()
        elif option == "3":
            self.add_good_habit()
        else:
            print("please enter a number between 1 and 3")
            self.add()

    def add_project(self):
        job = input("Enter the name of the project")
        points = int(input("How many points is this project worth ?"))
        self.add_projects(job, points)
        print("Project Added")
    def add_bad_habit(self):
        name = input("Enter the name of the bad habit")
        points = int(input("How many points is this bad habit worth(negative) ?"))
        self.add_bad_habits(name, points)
        print("Bad Habit Added")
    def add_good_habit(self):
        name = input("Enter the name of the good habit")
        points = int(input("How many points is this good habit worth ?"))
        self.add_good_habits(name, points)
        print("Good Habit Added")
    
    def remove(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit ?")
        
        if option == "1":
            self.remove_project()
        elif option == "2":
            self.remove_bad_habit()
        elif option == "3":
            self.remove_good_habit()
        else:
            print("please enter a number between 1 and 3")
            self.remove()

    def remove_project(self):
        iteration = 1
        for project in self.projects:
            print(f"{iteration}:  {project.job} - {project.points} - {project.completed}")
            iteration+=1
        option = input("Which Project would u like to remove ?")
        self.projects.pop(int(option)-1)
        print("Project Removed")
    def remove_bad_habit(self):
        iteration = 1
        for bad_habit in self.bad_habits:
            print(f"{iteration}:  {bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
            iteration+=1
        option = input("Which Bad Habit would u like to remove ?")
        self.bad_habits.pop(int(option)-1)
        print("Bad Habit Removed")
    def remove_good_habit(self):
        iteration = 1
        for good_habit in self.good_habits:
            print(f"{iteration}:  {good_habit.name} - {good_habit.points} - {good_habit.completed}")
            iteration+=1
        option = input("Which Good Habit would u like to remove ?")
        self.good_habits.pop(int(option)-1)
        print("Good Habit Removed")

    def show_points(self):
        print(f"U have {self.point_count} points")
    



app = GUI()
app.change()
app.show_all_Items()


    