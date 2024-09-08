
from PyQt6.QtWidgets import (QApplication,
                              QMainWindow, 
                              QPushButton, 
                              QVBoxLayout,
                              QHBoxLayout,
                              QWidget,
                              QColorDialog,
                               
                              QLabel,
                              QPushButton)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon

class QPallete(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(16,16))
        self.setIcon(QIcon("icons/pallete.png"))
    
    def choose_color(self):
        return QColorDialog().getColor()
