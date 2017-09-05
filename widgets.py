
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QTransform, QPainter

class World2D(QWidget):
    """A Widget which has it's own 2D world space, onto which shapes can be drawn.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.world_transform = QTransform()
        self._is_mouse_down = False

    def inverse_world_transform(self):
        return self.world_transform()

    def world_painter(self):
        painter = QPainter()
        painter.begin(self)
        painter.setWorldMatrixEnabled(True)
        painter.setWorldTransform(self.world_transform)

        return painter

    def mousePressEvent(self, mouse_event):
        super().mousePressEvent(mouse_event)

    def mouseReleaseEvent(self, mouse_event):
        super().mouseReleaseEvent(mouse_event)

    def mouseMoveEvent(self, mouse_event):
        super().mouseMoveEvent(mouse_event)
