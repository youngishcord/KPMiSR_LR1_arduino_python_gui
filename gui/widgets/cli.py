
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit


class Cli(QPlainTextEdit):
    # insertText() дополнение текста
    # setText() Замена текста
    def __init__(self, parent = None):
        super().__init__(parent)
        
        
        self.setReadOnly(True)
        self.setPlainText("Начало работы\n")
        
        