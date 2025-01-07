from PyQt6.QtWidgets import QInputDialog, QComboBox, QTabWidget, QApplication, QLineEdit, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QCheckBox, QLabel, QPushButton, QStackedWidget, QMenuBar, QMessageBox
from PyQt6.QtCore import Qt
import sys
import os

class Project:
    def __init__(self, job, points):
        self.job = job
        self.points = points
        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

class BadHabit:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

class GoodHabit:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

class Reward:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.point_count = 0
        self.projects = []
        self.bad_habits = []
        self.good_habits = []
        self.rewards = []

        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle('Motivation App')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.points_label = QLabel(f'Points: {self.point_count}')
        self.layout.addWidget(self.points_label)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.projects_tab = QWidget()
        self.bad_habits_tab = QWidget()
        self.good_habits_tab = QWidget()
        self.rewards_tab = QWidget()

        self.tab_widget.addTab(self.projects_tab, 'Projects')
        self.tab_widget.addTab(self.bad_habits_tab, 'Bad Habits')
        self.tab_widget.addTab(self.good_habits_tab, 'Good Habits')
        self.tab_widget.addTab(self.rewards_tab, 'Rewards')

        self.projects_layout = QVBoxLayout(self.projects_tab)
        self.bad_habits_layout = QVBoxLayout(self.bad_habits_tab)
        self.good_habits_layout = QVBoxLayout(self.good_habits_tab)
        self.rewards_layout = QVBoxLayout(self.rewards_tab)

        self.add_project_button = QPushButton('Add Project')
        self.add_project_button.clicked.connect(self.add_project)
        self.projects_layout.addWidget(self.add_project_button)

        self.add_bad_habit_button = QPushButton('Add Bad Habit')
        self.add_bad_habit_button.clicked.connect(self.add_bad_habit)
        self.bad_habits_layout.addWidget(self.add_bad_habit_button)

        self.add_good_habit_button = QPushButton('Add Good Habit')
        self.add_good_habit_button.clicked.connect(self.add_good_habit)
        self.good_habits_layout.addWidget(self.add_good_habit_button)

        self.add_reward_button = QPushButton('Add Reward')
        self.add_reward_button.clicked.connect(self.add_reward)
        self.rewards_layout.addWidget(self.add_reward_button)

        self.show_all_items()

    def add_project(self):
        job, ok = QInputDialog.getText(self, 'Add Project', 'Enter the name of the project:')
        if ok:
            points, ok = QInputDialog.getInt(self, 'Add Project', 'How many points is this project worth?')
            if ok:
                self.projects.append(Project(job, points))
                self.show_projects()

    def add_bad_habit(self):
        name, ok = QInputDialog.getText(self, 'Add Bad Habit', 'Enter the name of the bad habit:')
        if ok:
            points, ok = QInputDialog.getInt(self, 'Add Bad Habit', 'How many points is this bad habit worth (negative)?')
            if ok:
                self.bad_habits.append(BadHabit(name, points))
                self.show_bad_habits()

    def add_good_habit(self):
        name, ok = QInputDialog.getText(self, 'Add Good Habit', 'Enter the name of the good habit:')
        if ok:
            points, ok = QInputDialog.getInt(self, 'Add Good Habit', 'How many points is this good habit worth?')
            if ok:
                self.good_habits.append(GoodHabit(name, points))
                self.show_good_habits()

    def add_reward(self):
        name, ok = QInputDialog.getText(self, 'Add Reward', 'Enter the name of the reward:')
        if ok:
            price, ok = QInputDialog.getInt(self, 'Add Reward', 'How many points is this reward worth?')
            if ok:
                self.rewards.append(Reward(name, price))
                self.show_rewards()

    def show_all_items(self):
        self.show_projects()
        self.show_bad_habits()
        self.show_good_habits()
        self.show_rewards()

    def show_projects(self):
        for i in reversed(range(self.projects_layout.count())):
            widget = self.projects_layout.itemAt(i).widget()
            if widget and widget != self.add_project_button:
                widget.setParent(None)
        for project in self.projects:
            layout = QHBoxLayout()
            label = QLabel(f"{project.job} - {project.points} - {'Completed' if project.completed else 'Not Completed'}")
            layout.addWidget(label)
            if not project.completed:
                complete_button = QPushButton('Complete')
                complete_button.clicked.connect(lambda _, p=project: self.complete_project(p))
                layout.addWidget(complete_button)
            self.projects_layout.addLayout(layout)

    def show_bad_habits(self):
        for i in reversed(range(self.bad_habits_layout.count())):
            widget = self.bad_habits_layout.itemAt(i).widget()
            if widget and widget != self.add_bad_habit_button:
                widget.setParent(None)
        for bad_habit in self.bad_habits:
            layout = QHBoxLayout()
            label = QLabel(f"{bad_habit.name} - {bad_habit.points} - {'Completed' if bad_habit.completed else 'Not Completed'}")
            layout.addWidget(label)
            if not bad_habit.completed:
                complete_button = QPushButton('Complete')
                complete_button.clicked.connect(lambda _, bh=bad_habit: self.complete_bad_habit(bh))
                layout.addWidget(complete_button)
            self.bad_habits_layout.addLayout(layout)

    def show_good_habits(self):
        for i in reversed(range(self.good_habits_layout.count())):
            widget = self.good_habits_layout.itemAt(i).widget()
            if widget and widget != self.add_good_habit_button:
                widget.setParent(None)
        for good_habit in self.good_habits:
            layout = QHBoxLayout()
            label = QLabel(f"{good_habit.name} - {good_habit.points} - {'Completed' if good_habit.completed else 'Not Completed'}")
            layout.addWidget(label)
            if not good_habit.completed:
                complete_button = QPushButton('Complete')
                complete_button.clicked.connect(lambda _, gh=good_habit: self.complete_good_habit(gh))
                layout.addWidget(complete_button)
            self.good_habits_layout.addLayout(layout)

    def show_rewards(self):
        for i in reversed(range(self.rewards_layout.count())):
            widget = self.rewards_layout.itemAt(i).widget()
            if widget and widget != self.add_reward_button:
                widget.setParent(None)
        for reward in self.rewards:
            layout = QHBoxLayout()
            label = QLabel(f"{reward.name} - {reward.price}")
            layout.addWidget(label)
            buy_button = QPushButton('Buy')
            buy_button.clicked.connect(lambda _, r=reward: self.buy_reward(r))
            layout.addWidget(buy_button)
            self.rewards_layout.addLayout(layout)

    def load_data(self):
        if os.path.exists("save.txt") and os.path.getsize("save.txt") > 0:
            with open("save.txt", "r") as file:
                lines = file.readlines()
                self.point_count = int(lines[0])
                self.points_label.setText(f'Points: {self.point_count}')

                mode = None
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith("Projects:"):
                        mode = "project"
                        line = line.replace("Projects:", "").strip()
                    elif line.startswith("Bad Habits:"):
                        mode = "bad_habit"
                        line = line.replace("Bad Habits:", "").strip()
                    elif line.startswith("Good Habits:"):
                        mode = "good_habit"
                        line = line.replace("Good Habits:", "").strip()
                    elif line.startswith("Rewards:"):
                        mode = "reward"
                        line = line.replace("Rewards:", "").strip()

                    if mode == "project":
                        job, points, completed = line.split(" - ")
                        proj = Project(job, int(points))
                        if completed == "True":
                            proj.complete()
                        self.projects.append(proj)
                    elif mode == "bad_habit":
                        name, points, completed = line.split(" - ")
                        bh = BadHabit(name, int(points))
                        if completed == "True":
                            bh.complete()
                        self.bad_habits.append(bh)
                    elif mode == "good_habit":
                        name, points, completed = line.split(" - ")
                        gh = GoodHabit(name, int(points))
                        if completed == "True":
                            gh.complete()
                        self.good_habits.append(gh)
                    elif mode == "reward":
                        name, price = line.split(" - ")
                        self.rewards.append(Reward(name, int(price)))

        self.show_all_items()

    def save_data(self):
        with open("save.txt", "w") as file:
            file.write(f"{self.point_count}\n")
            for project in self.projects:
                file.write(f"Projects:{project.job} - {project.points} - {project.completed}\n")
            for bad_habit in self.bad_habits:
                file.write(f"Bad Habits:{bad_habit.name} - {bad_habit.points} - {bad_habit.completed}\n")
            for good_habit in self.good_habits:
                file.write(f"Good Habits:{good_habit.name} - {good_habit.points} - {good_habit.completed}\n")
            for reward in self.rewards:
                file.write(f"Rewards:{reward.name} - {reward.price}\n")
        print("Data Saved")

    def complete_project(self, project):
        project.complete()
        self.point_count += project.points
        self.points_label.setText(f'Points: {self.point_count}')
        self.show_projects()
        self.save_data()

    def complete_bad_habit(self, bad_habit):
        bad_habit.complete()
        self.point_count += bad_habit.points
        self.points_label.setText(f'Points: {self.point_count}')
        self.show_bad_habits()
        self.save_data()

    def complete_good_habit(self, good_habit):
        good_habit.complete()
        self.point_count += good_habit.points
        self.points_label.setText(f'Points: {self.point_count}')
        self.show_good_habits()
        self.save_data()

    def buy_reward(self, reward):
        if self.point_count >= reward.price:
            self.point_count -= reward.price
            self.points_label.setText(f'Points: {self.point_count}')
            self.rewards.remove(reward)
            self.show_rewards()
            self.save_data()
        else:
            QMessageBox.warning(self, 'Not enough points', 'You do not have enough points to buy this reward.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())