import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit, QSlider
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice, Signal, Slot, Qt


class StepController(QWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)
        
        self.lay.addWidget(QtWidgets.QLabel("Управление шаговым двигателем"))
        
        self.min_widget = QtWidgets.QSpinBox()
        self.min_widget.setMinimum(-100)
        self.min_widget.setMaximum(-1)
        self.min_widget.setValue(-10)
        self.min_widget.valueChanged.connect(self.change_min)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.change_current)
        # self.slider.sliderReleased.connect(self._write_command)
        
        self.max_widget = QtWidgets.QSpinBox()
        self.max_widget.setMinimum(1)
        self.max_widget.setMaximum(100)
        self.max_widget.setValue(10)
        self.max_widget.valueChanged.connect(self.change_max)
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.min_widget)
        layout.addWidget(self.slider)
        layout.addWidget(self.max_widget)
        self.lay.addLayout(layout)
        
        self.current_angle = QtWidgets.QSpinBox()
        self.current_angle.setMinimum(self.min_widget.value())
        self.current_angle.setMaximum(self.max_widget.value())
        self.current_angle.valueChanged.connect(self.change_current)
        
        self.lay.addWidget(self.current_angle)
        
        self.start_step = QtWidgets.QPushButton("Начать движение")
        self.start_step.clicked.connect(self._write_command)
        self.lay.addWidget(self.start_step)
        

    @Slot(int)
    def change_min(self, val):
        self.current_angle.setMinimum(val)
        self.slider.setMinimum(val)

    @Slot(int)
    def change_max(self, val):
        self.current_angle.setMaximum(val)
        self.slider.setMaximum(val)

    @Slot(int)
    def change_current(self, val):
        self.current_angle.setValue(val)
        self.slider.setValue(val)


    def _write_command(self):
        self.log_message.emit(f"Шаговый выставлен на {self.current_angle.value()}")
        self.write_command.emit(f"StepperSet {self.current_angle.value()}")
        self.current_angle.setValue(0)
