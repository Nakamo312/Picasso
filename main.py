import sys
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QVBoxLayout, 
                             QWidget, 
                             QToolBar, 
                             QLabel,
                             QSlider)

# from color_pallete_widget import ColorPalleteWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap

from canvas import Canvas
from color_pallete_widget import QPallete



class CustomWindow(QMainWindow):
    def __init__(self, title, w, h):
        super().__init__()
        self.count = 0
        self.setFixedSize(QSize(w,h))
        self.setWindowTitle(title)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.btn_color = QPallete()
        self.erase_widget = QPushButton()
        self.erase_widget.setIcon(QIcon("icons/eraser.png"))
        self.v1 = QVBoxLayout()
        self.central_widget.setLayout(self.v1)
        self.btn_color.clicked.connect(self.choose_color)
        self.erase_widget.clicked.connect(self.set_erase_color)
        #инициализация холста
        self.canvas = Canvas(800,600)
        self.v1.addWidget(self.canvas)
        self.v1.addWidget(self.btn_color)
        #инициализация тулбара слайдера
        self.sliderToolBar = QToolBar(self)
        self.sliderToolBar.setIconSize(QSize(16,16))
        self.sliderToolBar.setObjectName("slider")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.sliderToolBar)
        self.pen_size_slider = QSlider()
        self.pen_size_slider.setRange(10,30)
        self.pen_size_slider.setOrientation(Qt.Orientation.Horizontal)
        sizeIcon = QLabel()
        sizeIcon.setPixmap(QPixmap("icons/border-weight.png"))
        self.sliderToolBar.addWidget(sizeIcon)
        self.sliderToolBar.addWidget(self.pen_size_slider)
        self.pen_size_slider.valueChanged.connect(self.set_size)

         #инициализация тулбара палитры
        self.palleteToolBar = QToolBar(self)
        self.palleteToolBar.setIconSize(QSize(16,16))
        self.palleteToolBar.setObjectName("pallete")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.palleteToolBar)

        self.palleteToolBar.addWidget(self.btn_color)

         #инициализация тулбара палитры
        self.eraseToolBar = QToolBar(self)
        self.eraseToolBar.setIconSize(QSize(16,16))
        self.eraseToolBar.setObjectName("erase")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.eraseToolBar)

        self.eraseToolBar.addWidget(self.erase_widget)


                #инициализация меню
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        new_img = QAction(QIcon("icons/new-image.png"), "New", self)
        open_img = QAction(QIcon("icons/open-image.png"), "Open", self)
        save_img = QAction(QIcon("icons/save-image.png"), "Save", self)
        file_menu.addAction(new_img)
        file_menu.addAction(open_img)
        file_menu.addAction(save_img)

    def choose_color(self):
        self.canvas.pen_color = self.btn_color.choose_color()
    
    def set_erase_color(self):
        ...

    def set_size(self, value):
        self.canvas.pen_size = value


app = QApplication(sys.argv)
window =  CustomWindow("Picasso", 800, 600)
window.show()
app.exec()
