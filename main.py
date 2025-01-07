from PyQt6.QtWidgets import QComboBox,QTabWidget,QApplication,QLineEdit, QMainWindow,QHBoxLayout,QVBoxLayout , QVBoxLayout, QWidget, QCheckBox, QLabel, QPushButton, QStackedWidget, QMenuBar, QMessageBox
from PyQt6.QtCore import Qt
import sys
import os

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

class rewards:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    


class GUI:
    def __init__(self):
        self.point_count = 0
        self.projects = []
        self.bad_habits = []
        self.good_habits = []
        self.rewards = []

        self.load_data()
        self.change()
        self.show_all_Items()
        
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
                        option = input("Would u like to open the shop ? (y/n)")
                        if option == "y":
                            self.open_shop()
                        else:
                            option = input("would u like to close the program ? (y/n)")
                            if option == "y":
                                self.save_data()
                                print("Goodbye")    
                            else:
                                self.change()
    
        
    def complete(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit or 4/nothing ?")
        
        if option == "1":
            self.complete_project()
        elif option == "2":
            self.complete_bad_habit()
        elif option == "3":
            self.complete_good_habit()
        elif option == "4":
            self.change()
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
        option = input("Would u like to complete another project ? (y/n)")
        if option == "y":
            self.complete_project()
        else:
            self.change()
    def complete_bad_habit(self):
        iteration = 1
        for bad_habit in self.bad_habits:
            print(f"{iteration}:  {bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
            iteration+=1
        option = input("Which Bad Habit would u like to complete ?")
        self.point_count
        self.bad_habits[int(option)-1].complete()
        print("Bad Habit failed")
        option = input("Would u like to complete another project ? (y/n)")
        if option == "y":
            self.complete_project()
        else:
            self.change() 
    def complete_good_habit(self):

        iteration = 1
        for good_habit in self.good_habits:
            print(f"{iteration}:  {good_habit.name} - {good_habit.points} - {good_habit.completed}")
            iteration+=1
        option = input("Which Good Habit would u like to complete ?")
        self.point_count += self.good_habits[int(option)-1].points
        self.good_habits[int(option)-1].complete()
        print("Good Habit Completed")
        option = input("Would u like to complete another project ? (y/n)")
        if option == "y":
            self.complete_project()
        else:
            self.change()

    def add(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit or 4/nothing?")
        if option == "1":
            self.add_project()
        elif option == "2":
            self.add_bad_habit()
        elif option == "3":
            self.add_good_habit()
        elif option == "4":
            self.change()
        else:
            print("please enter a number between 1 and 3")
            self.add()

    def add_project(self):
        job = input("Enter the name of the project:")
        points = int(input("How many points is this project worth ?"))
        self.add_projects(job, points)
        print("Project Added")
        option = input("Would u like to add another project ? (y/n)")
        if option == "y":
            self.add_project()
        else:
            self.change()
    def add_bad_habit(self):
        name = input("Enter the name of the bad habit:")
        points = int(input("How many points is this bad habit worth(negative) ?"))
        self.add_bad_habits(name, points)
        print("Bad Habit Added")
        option = input("Would u like to add another project ? (y/n)")
        if option == "y":
            self.add_project()
        else:
            self.change()
    def add_good_habit(self):
        name = input("Enter the name of the good habit:")
        points = int(input("How many points is this good habit worth ?"))
        self.add_good_habits(name, points)
        print("Good Habit Added")
        option = input("Would u like to add another project ? (y/n)")
        if option == "y":
            self.add_project()
        else:
            self.change()
    
    def remove(self):
        option= input ("Would U like to add 1/ a project 2/ a bad habit 3/ a good habit or 4/nothing?")
        
        if option == "1":
            self.remove_project()
        elif option == "2":
            self.remove_bad_habit()
        elif option == "3":
            self.remove_good_habit()
        elif option == "4":
            self.change()
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
        option = input("Would u like to remove another project ? (y/n)")   
        if option == "y":
            self.remove_project()
        else:
            self.change()
    def remove_bad_habit(self):
        iteration = 1
        for bad_habit in self.bad_habits:
            print(f"{iteration}:  {bad_habit.name} - {bad_habit.points} - {bad_habit.completed}")
            iteration+=1
        option = input("Which Bad Habit would u like to remove ?")
        self.bad_habits.pop(int(option)-1)
        print("Bad Habit Removed")
        option = input("Would u like to remove another project ? (y/n)")   
        if option == "y":
            self.remove_project()
        else:
            self.change()
    def remove_good_habit(self):
        iteration = 1
        for good_habit in self.good_habits:
            print(f"{iteration}:  {good_habit.name} - {good_habit.points} - {good_habit.completed}")
            iteration+=1
        option = input("Which Good Habit would u like to remove ?")
        self.good_habits.pop(int(option)-1)
        print("Good Habit Removed")
        option = input("Would u like to remove another project ? (y/n)")   
        if option == "y":
            self.remove_project()
        else:
            self.change()

    def show_points(self):
        print(f"U have {self.point_count} points")
    
    def save_data(self):
        file1 = open("save.txt", "w")
        file1.write(f"{self.point_count}\n")
        for project in self.projects:
            file1.write(f"Projects:")
            file1.write(f"{project.job} - {project.points} - {project.completed}\n")
        for bad_habit in self.bad_habits:
            file1.write(f"Bad Habits:")
            file1.write(f"{bad_habit.name} - {bad_habit.points} - {bad_habit.completed}\n")
        for good_habit in self.good_habits:
            file1.write(f"Good Habits:")
            file1.write(f"{good_habit.name} - {good_habit.points} - {good_habit.completed}\n")
        for reward in self.rewards:
            file1.write(f"Rewards:")
            file1.write(f"{reward.name} - {reward.price}\n") 
        file1.close()
        print("Data Saved") 
    
    def load_data(self):
        if os.path.exists("save.txt") and os.path.getsize("save.txt") > 0:
            file1 = open("save.txt", "r")
            lines = file1.readlines()          
            self.point_count = int(lines[0])

            mode = None
            for line in lines[1:]:
                line = line.strip()
                if line.startswith("Projects:"):
                    mode = "project"    
                    line = line.replace("Projects:", "")             
                elif line.startswith("Bad Habits:"):
                    mode = "bad_habit"   
                    line = line.replace("Bad Habits:", "")              
                elif line.startswith("Good Habits:"):
                    mode = "good_habit"     
                    line = line.replace("Good Habits:", "")              
                elif line.startswith("Rewards:"):
                    mode = "reward"
                    line = line.replace("Rewards:", "")
                    
                if mode == "project":
                    job, points, completed = line.split(" - ")
                    proj = project(job, int(points))
                    if completed == "True":
                        proj.complete()
                    self.projects.append(proj)                   
                elif mode == "bad_habit":
                    name, points, completed = line.split(" - ")
                    bh = bad_habit(name, int(points))
                    if completed == "True":
                        bh.complete()
                    self.bad_habits.append(bh)
                elif mode == "good_habit":
                    name, points, completed = line.split(" - ")
                    gh = good_habit(name, int(points))                   
                    if completed == "True":
                        gh.complete()
                    self.good_habits.append(gh)
                elif mode == "reward":
                    name, price = line.split(" - ")
                    self.rewards.append(rewards(name, int(price)))
        file1.close()
        self.show_all_Items()
                                         
        

    def open_shop(self):
        print("Welcome to the shop")
        print("Here are the rewards")
        option = input("Would u like to buy any ? (y/n)")
        if option == "y":
            self.buy()
        else:
            option = input("Would u like to add a reward? (y/n)")
            if option == "y":
                self.add_reward()
            else:
                self.change()
        
    def buy(self):
        iteration = 1
        for reward in self.rewards:
            print(f"{iteration}:  {reward.name} - {reward.price}")
            iteration+=1
        option = input("Which Reward would u like to buy ?")
        if self.point_count >= self.rewards[int(option)-1].price:
            self.point_count -= self.rewards[int(option)-1].price
            print("Reward Bought")
        else:
            print("Not enough points")
        option = input("Would u like to buy another reward ? (y/n)")
        if option == "y":
            self.buy()
        else:
            self.open_shop()
    
    def add_reward(self):
        name = input("Enter the name of the reward")
        price = int(input("How many points is this reward worth ?"))
        self.rewards.append(rewards(name, price))
        print("Reward Added")
        option = input("Would u like to add another reward ? (y/n)")
        if option == "y":
            self.add_reward()
        else:
            self.open_shop()
        


app = GUI()



    