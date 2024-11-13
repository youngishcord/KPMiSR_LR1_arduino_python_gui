
import sys

import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication

from src.controller import Controller
from widgets.tasks_tab import TasksTabs
from widgets.cli import Cli
from widgets.settings import Settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа 1")

        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_lay)

        self.tasks = TasksTabs()
        self.main_lay.addWidget(self.tasks)

        self.settings_lay = QtWidgets.QHBoxLayout()
        self.main_lay.addLayout(self.settings_lay)

        self.cli = Cli()
        self.settings_lay.addWidget(self.cli)

        self.controller = Controller()
        

        self.settings = Settings()
        self.settings_lay.addWidget(self.settings)
        
        self.setup_signals()


    def setup_signals(self):
        self.controller.log_message.connect(self.cli.log_message)
        
        self.settings.log_message.connect(self.cli.log_message)
        self.settings.on_connect.connect(self.controller.open_port)
        self.settings.on_disconnect.connect(self.controller.close_port)
        self.settings.write_command.connect(self.controller.write_command)
        
        self.controller.update_state.connect(self.settings.update_state)
        
        self.tasks.log_message.connect(self.cli.log_message)
        self.tasks.write_command.connect(self.controller.write_command)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
