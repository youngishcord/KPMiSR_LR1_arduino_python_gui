
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice


class Settings(QWidget):
    # insertText() дополнение текста
    # setText() Замена текста
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.lay = QtWidgets.QGridLayout()
        self.setLayout(self.lay)
        
        self.lay.addWidget()
        
        self.update_bt = QtWidgets.QPushButton("Update")
        self.lay.addWidget(self.update_bt, 0, 0)
        
        self.serial = QSerialPort()
        
        self.port = QtWidgets.QComboBox()
        self.port.addItems(["test1", "test2"])
        self.lay.addWidget(self.port)
        