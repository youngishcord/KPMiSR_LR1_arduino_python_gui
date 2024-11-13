import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice, Signal, Slot, QByteArray


class LedController(QWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.lay = QtWidgets.QHBoxLayout()
        self.setLayout(self.lay)
        
        self.lay.addLayout(self.create_color("Красный", "red"))
        self.lay.addLayout(self.create_color("Зеленый", "green"))
        self.lay.addLayout(self.create_color("Синий", "blue"))
        # self.lay.addLayout(self.create_color("черный", "black"))
        
    
    def create_color(self, name: str, color: str) -> QtWidgets.QVBoxLayout:
        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(QtWidgets.QLabel(name))
        
        color_widget = QtWidgets.QLabel()
        color_widget.setStyleSheet(f"background-color: {color};")
        lay.addWidget(color_widget)
        
        pb = QtWidgets.QPushButton("Переключатель")
        pb.setCheckable(True)
        pb.clicked.connect(lambda: self.swich_led(pb.isChecked(), name, color))
        lay.addWidget(pb)
        return lay
        
        
    def swich_led(self, state, name, color):
        self.log_message.emit(f"Изменено состояние светодиода {name} {1 if state else 0}")
        self.write_command.emit(f"SetLed {color} {1 if state else 0}")
        