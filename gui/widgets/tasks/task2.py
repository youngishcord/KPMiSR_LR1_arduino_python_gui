import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit, QSlider
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice, Signal, Slot, Qt


class ServController(QWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)
        
        self.lay.addWidget(QtWidgets.QLabel("Управление сервоприводом"))
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.valueChanged.connect(self.change_current)
        self.slider.sliderReleased.connect(self._write_command)
        
        self.max_widget = QtWidgets.QSpinBox()
        self.max_widget.setMinimum(0)
        self.max_widget.setMaximum(2048)
        self.max_widget.setValue(180)
        self.max_widget.valueChanged.connect(self.change_max)
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.max_widget)
        self.lay.addLayout(layout)
        
        self.current_angle = QtWidgets.QSpinBox()
        self.current_angle.setMinimum(0)
        self.current_angle.setMaximum(self.max_widget.value())
        self.current_angle.valueChanged.connect(self.change_current)
        
        self.lay.addWidget(self.current_angle)


    @Slot(int)
    def change_max(self, val):
        self.current_angle.setMaximum(val)
        self.slider.setMaximum(val)
        

    @Slot(int)
    def change_current(self, val):
        self.current_angle.setValue(val)
        self.slider.setValue(val)
        
        
    def _write_command(self):
        self.log_message.emit("text")
        self.write_command.emit("text")


    def swich_led(self, state, name, color):
        self.log_message.emit(f"Изменено состояние светодиода {name} {state}")
        self.write_command.emit(f"SetLed {color} {state}")
        