
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Signal, Slot

from widgets.tasks.task1 import LedController


class TasksTabs(QtWidgets.QTabWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.led_controller = LedController()
        self.addTab(self.led_controller, "Контроллет светодиодов")
        self.led_controller.log_message.connect(self.log_message.emit)
        # self.addTab(None, "test2")
        
        