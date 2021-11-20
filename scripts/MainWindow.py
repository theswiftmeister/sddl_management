from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from guipy.main_window import MainWindow


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
