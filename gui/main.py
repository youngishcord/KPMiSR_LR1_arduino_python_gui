import sys

import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication

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
        
        self.settings = Settings()
        self.settings_lay.addWidget(self.settings)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()