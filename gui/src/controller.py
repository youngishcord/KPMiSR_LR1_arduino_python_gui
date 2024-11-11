
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Signal, Slot, QIODevice


class Controller(QWidget):
    log_message = Signal(str)
    update_state = Signal(bool)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.connection_state = False
        self.serial = QSerialPort()
        self.serial.errorOccurred.connect(self.handle_error)
        
        
    @Slot(str, int)
    def open_port(self, port_name:str, port_speed:int):
        if self.serial.isOpen():
            self.log_message.emit("Подключение уже установлено")
            return
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(port_speed)
        self.serial.open(QIODevice.OpenModeFlag.ReadWrite)
        self.log_message.emit(f"Подключение к порту {port_name}, скорость {port_speed}")
        if not self.serial.isOpen():
            self.log_message.emit("Подключение не было установлено")
            return
        self.connection_state = True
        self.update_state.emit(self.connection_state)
        
        
    @Slot()
    def close_port(self):
        if not self.serial.isOpen():
            self.log_message.emit("Подключение отсутствует")
            return
        self.log_message.emit("Отключение")
        self.serial.close()
        self.connection_state = False
        self.update_state.emit(self.connection_state)
        
        
    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.ResourceError:
            # Плохо работает
            self.log_message.emit("Потеряно соединение")
            if self.serial.isOpen():
                self.serial.close()
                self.connection_state = False
                self.update_state.emit(self.connection_state)
        elif error == QSerialPort.PermissionError:
            self.log_message.emit("Потеряно соединение")
            if self.serial.isOpen():
                self.serial.close()
                self.connection_state = False
                self.update_state.emit(self.connection_state)
        elif error == QSerialPort.NoError:
            return
        else:
            # self.log_message.emit(error)
            print("В КОНТРОЛЛЕРЕ ВЫЗВАНО НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ")
            print(error)
