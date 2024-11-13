
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice, Signal, Slot


TEST = 1

class Settings(QWidget):
    log_message = Signal(str)
    on_connect = Signal(str, int)
    on_disconnect = Signal()
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.lay = QtWidgets.QGridLayout()
        self.setLayout(self.lay)
        
        self.lay.addWidget(QtWidgets.QLabel("Панель подключения"), 0, 0)
        self.lay.addWidget(QtWidgets.QLabel("Порт подключения:"), 1, 0)
        
        self.ports = QtWidgets.QComboBox()
        self.lay.addWidget(self.ports, 2, 0)
        
        self.lay.addWidget(QtWidgets.QLabel("Скорость подключения:"), 1, 1)
        
        self.speed = QtWidgets.QComboBox()
        self.lay.addWidget(self.speed, 2, 1)
        
        self.update_bt = QtWidgets.QPushButton("Обновить")
        self.lay.addWidget(self.update_bt, 0, 1)
        self.update_bt.clicked.connect(self.update_settings)
        
        self.connect_bt = QtWidgets.QPushButton("Подключиться")
        self.lay.addWidget(self.connect_bt)
        self.connect_bt.clicked.connect(self._on_connect)
        
        self.disconnect_bt = QtWidgets.QPushButton("Отключиться")
        self.lay.addWidget(self.disconnect_bt)
        self.disconnect_bt.clicked.connect(self._on_disconnect)
        
        self.state_widget = QtWidgets.QLabel()
        self.lay.addWidget(self.state_widget, 4, 0, 1, 2)
        self.state_widget.setStyleSheet("background-color: red;")

        if TEST:
            self.test_bt = QtWidgets.QPushButton("TEST")
            self.lay.addWidget(self.test_bt)
            self.test_bt.clicked.connect(self._on_test)
        
        self.update_settings()
        
    def _on_test(self):
        self.write_command.emit("Test 1\0")

    @Slot()
    def _on_connect(self):
        self.on_connect.emit(self.ports.currentText(), int(self.speed.currentText()))
        
    def _on_disconnect(self):
        self.on_disconnect.emit()

    def update_settings(self):
        self.ports.clear()
        self.speed.clear()
        
        self.log_message.emit("Обновление данных")
        self.ports.addItems([port.portName() for port in QSerialPortInfo.availablePorts()])
        
        self.speed.addItems(map(str, QSerialPortInfo.standardBaudRates()))
        
    @Slot(bool)
    def update_state(self, state):
        self.state_widget.setStyleSheet(f"background-color: {'green' if state else 'red'};")