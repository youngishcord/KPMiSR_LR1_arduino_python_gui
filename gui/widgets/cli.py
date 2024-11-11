
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtCore import Signal, Slot


class Cli(QPlainTextEdit):
    # insertText() дополнение текста
    # setText() Замена текста
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setReadOnly(True)
        self.setPlainText("Начало работы")


    @Slot(str)
    def log_message(self, message):
        self.appendPlainText("> " + message)
        
    
    @Slot()
    def clear_console(self):
        self.clear()
