
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice


class TasksTabs(QtWidgets.QTabWidget):
    # insertText() дополнение текста
    # setText() Замена текста
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.addTab(None, "test1")
        self.addTab(None, "test2")
        