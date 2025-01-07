from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QLabel, QPushButton, QStackedWidget, QMenuBar, QMessageBox

class TrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkmark Tracker")

        self.points = 0

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        self.create_habits_tab()
        self.create_projects_tab()
        self.create_bad_habits_tab()
        self.create_settings_tab()

        self.create_menu()

    def safe_data(self):
        with open("data.txt", "w") as file:
            file.write(str(self.points))
            file.write("\n")
            file.write(str(self.habit1_check.isChecked()))

    def create_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        habits_action = menu_bar.addAction("Habits")
        habits_action.triggered.connect(lambda: self.show_tab(0))

        projects_action = menu_bar.addAction("Projects")
        projects_action.triggered.connect(lambda: self.show_tab(1))

        bad_habits_action = menu_bar.addAction("Bad Habits")
        bad_habits_action.triggered.connect(lambda: self.show_tab(2))

        settings_action = menu_bar.addAction("Settings")
        settings_action.triggered.connect(lambda: self.show_tab(3))

    def create_habits_tab(self):
        habits_tab = QWidget()
        layout = QVBoxLayout(habits_tab)

        label = QLabel("Habits Tracker")
        layout.addWidget(label)

        self.habit1_check = QCheckBox("Exercise")
        self.habit1_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.habit1_check)

        self.habit2_check = QCheckBox("Meditate")
        self.habit2_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.habit2_check)

        self.habit3_check = QCheckBox("Read a book")
        self.habit3_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.habit3_check)

        self.stack.addWidget(habits_tab)

    def create_projects_tab(self):
        projects_tab = QWidget()
        layout = QVBoxLayout(projects_tab)

        label = QLabel("Projects Tracker")
        layout.addWidget(label)

        self.project1_check = QCheckBox("Finish Report")
        self.project1_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.project1_check)

        self.project2_check = QCheckBox("Complete Presentation")
        self.project2_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.project2_check)

        self.stack.addWidget(projects_tab)

    def create_bad_habits_tab(self):
        bad_habits_tab = QWidget()
        layout = QVBoxLayout(bad_habits_tab)

        label = QLabel("Bad Habits Tracker")
        layout.addWidget(label)

        self.bad_habit1_check = QCheckBox("Procrastinate")
        self.bad_habit1_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.bad_habit1_check)

        self.bad_habit2_check = QCheckBox("Overeat")
        self.bad_habit2_check.stateChanged.connect(self.update_points)
        layout.addWidget(self.bad_habit2_check)

        self.stack.addWidget(bad_habits_tab)

    def create_settings_tab(self):
        settings_tab = QWidget()
        layout = QVBoxLayout(settings_tab)

        label = QLabel("Settings")
        layout.addWidget(label)

        reset_button = QPushButton("Reset Points")
        reset_button.clicked.connect(self.reset_points)
        layout.addWidget(reset_button)

        self.stack.addWidget(settings_tab)

    def show_tab(self, index):
        self.stack.setCurrentIndex(index)

    def update_points(self):
        self.points = 0

        if self.habit1_check.isChecked():
            self.points += 10

        if self.habit2_check.isChecked():
            self.points += 10

        if self.habit3_check.isChecked():
            self.points += 10

        if self.project1_check.isChecked():
            self.points += 20

        if self.project2_check.isChecked():
            self.points += 20

        if self.bad_habit1_check.isChecked():
            self.points -= 15

        if self.bad_habit2_check.isChecked():
            self.points -= 15

        QMessageBox.information(self, "Points Updated", f"Current Points: {self.points}")

    def reset_points(self):
        self.points = 0
        self.habit1_check.setChecked(False)
        self.habit2_check.setChecked(False)
        self.habit3_check.setChecked(False)
        self.project1_check.setChecked(False)
        self.project2_check.setChecked(False)
        self.bad_habit1_check.setChecked(False)
        self.bad_habit2_check.setChecked(False)
        QMessageBox.information(self, "Points Reset", "All points have been reset to 0.")

if __name__ == "__main__":
    app = QApplication([])
    tracker_app = TrackerApp()
    tracker_app.show()
    app.exec()
