import sys
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QVBoxLayout, 
                             QWidget, 
                             QToolBar, 
                             QLabel,
                             QSlider, QGroupBox, QGridLayout)

# from color_pallete_widget import ColorPalleteWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap, QColor

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

        self.tools = QWidget()
        form_layout = QGridLayout()
        vertical_layout = QVBoxLayout()
        self.erase_widget = QPushButton()
        self.erase_widget.setIcon(QIcon("icons/eraser.png"))

        self.brush_widget = QPushButton()
        self.brush_widget.setIcon(QIcon("icons/paint-brush.png"))

        self.can_widget = QPushButton()
        self.can_widget.setIcon(QIcon("icons/paint-can.png"))
        label = QLabel("tools")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.erase_widget, 1, 1)
        form_layout.addWidget(self.brush_widget, 1, 2)
        form_layout.addWidget(self.can_widget, 1, 3)
        vertical_layout.addLayout(form_layout)
        vertical_layout.addWidget(label)
        self.tools.setLayout(vertical_layout)

        self.color_tools = QGroupBox()
        form_layout = QGridLayout()
        vertical_layout = QVBoxLayout()
        self.btn_color = QPallete()

        label = QLabel("colors")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.btn_color,1,1)
        vertical_layout.addLayout(form_layout)
        vertical_layout.addWidget(label)
        self.color_tools.setLayout(vertical_layout)

        self.v1 = QVBoxLayout()
        self.central_widget.setLayout(self.v1)
        self.btn_color.clicked.connect(self.choose_color)
        self.erase_widget.clicked.connect(self.set_erase_color)
        self.brush_widget.clicked.connect(self.set_brush_color)
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

         #инициализация тулбара инструментов
        self.eraseToolBar = QToolBar(self)
        self.eraseToolBar.setIconSize(QSize(16,16))
        self.eraseToolBar.setObjectName("tools")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.eraseToolBar)

        self.eraseToolBar.addWidget(self.tools)

                 #инициализация тулбара палитры
        self.palleteToolBar = QToolBar(self)
        self.palleteToolBar.setIconSize(QSize(16,16))
        self.palleteToolBar.setObjectName("pallete")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.palleteToolBar)

        self.palleteToolBar.addWidget(self.color_tools)

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
        self.canvas.pen_color_cashed = self.canvas.pen_color
        self.canvas.pen_color = QColor(255,255,255)

    def set_brush_color(self):
        self.canvas.pen_color = self.canvas.pen_color_cashed

    def set_size(self, value):
        self.canvas.pen_size = value


app = QApplication(sys.argv)
window =  CustomWindow("Picasso", 800, 600)
window.show()
app.exec()
