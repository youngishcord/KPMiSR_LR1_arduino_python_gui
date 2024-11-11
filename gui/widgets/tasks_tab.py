
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Signal, Slot

from widgets.tasks.task1 import LedController
from widgets.tasks.task2 import ServoController
from widgets.tasks.task3 import StepController


class TasksTabs(QtWidgets.QTabWidget):
    log_message = Signal(str)
    write_command = Signal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.led_controller = LedController()
        self._setup_widget(self.led_controller, "Контроллер светодиодов")
        
        self.serv_controller = ServoController()
        self._setup_widget(self.serv_controller, "Контроллер сервопривода")
        
        self.step_controller = StepController()
        self._setup_widget(self.step_controller, "Контроллер шаговика")
        
    def _setup_widget(self, widget_, name):
        self.addTab(widget_, name)
        widget_.log_message.connect(self._log_emmiter)
        widget_.write_command.connect(self._write_emmiter)


    def _log_emmiter(self, data: str):
        self.log_message.emit(data)
        
    def _write_emmiter(self, data: str):
        self.write_command.emit(data)