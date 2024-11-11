
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Signal, Slot

from widgets.tasks.task1 import LedController
from widgets.tasks.task2 import ServController


class TasksTabs(QtWidgets.QTabWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.led_controller = LedController()
        self._setup_widget(self.led_controller, "Контроллет светодиодов")
        
        self.serv_controller = ServController()
        self._setup_widget(self.serv_controller, "Контроллет сервопривода")

        
    def _setup_widget(self, widget_, name):
        self.addTab(widget_, name)
        widget_.log_message.connect(self._log_emmiter)
        widget_.write_command.connect(self._write_emmiter)


    def _log_emmiter(self, data: str):
        self.log_message.emit(data)
        
    def _write_emmiter(self, data: str):
        self.write_command.emit(data)