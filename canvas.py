from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMouseEvent, QPixmap, QColor, QPainter
from PyQt6.QtCore import Qt
class Canvas(QLabel):
    def __init__(self, w: int, h: int):
        super().__init__()

        #НАСТРОЙКИ ПЕРА 
        self.x_mouse: int = None
        self.y_mouze: int = None
        self.pen_size: int = 4
        self.pen_color = QColor("#00000")
        pixmap = QPixmap(w,h)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)
        self.label = QLabel()
        self.set_text("ACTION")
        self.set_font_size(30)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.label)
        self.setLayout(self.v1)

    def set_pen_size(self, size: int):
        self.pen_size = size
        
    def set_text(self, text: str):
        self.label.setText(text)

    def set_font_size(self, size: int):
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def mouseMoveEvent(self, e: QMouseEvent):
        if self.x_mouse is None:
            self.x_mouse = e.position().x()
            self.y_mouse = e.position().y()
        
        canvas = self.pixmap()
        painter = QPainter(canvas)
        p = painter.pen()
        p.setWidth(self.pen_size)
        p.setColor(self.pen_color)
        painter.setPen(p)

        painter.drawLine(int(self.x_mouse), int(self.y_mouse), int(e.position().x()),int(e.position().y()))
        painter.end()
        self.setPixmap(canvas)
        self.x_mouse = e.position().x()
        self.y_mouse = e.position().y()

    def mouseReleaseEvent(self, ev: QMouseEvent | None) -> None:
        self.x_mouse = None
        self.y_mouse = None
