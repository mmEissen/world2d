
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QTransform, QPainter

class World2D(QWidget):
    """A Widget which has it's own 2D world space, onto which shapes can be drawn.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.world_transform = QTransform()
        self.zoom_base = 1.001
        self._is_mouse_down = False
        self._last_mouse_pos = QPoint()

    def inverse_world_transform(self):
        inverted, _ = self.world_transform.inverted()
        return inverted

    def world_painter(self):
        painter = QPainter()
        painter.begin(self)
        painter.setWorldMatrixEnabled(True)
        painter.setWorldTransform(self.world_transform)

        return painter

    def translate(self, dx, dy):
        self.world_transform.translate(dx, dy)
        self.update()

    def zoom(self, amount):
        self.world_transform.scale(amount, amount)
        self.update()

    def wheelEvent(self, wheel_event):
        super().wheelEvent(wheel_event)
        zoom_amount = self.zoom_base ** wheel_event.angleDelta().y()
        self.zoom(zoom_amount)

    def mousePressEvent(self, mouse_event):
        super().mousePressEvent(mouse_event)
        self._last_mouse_pos = mouse_event.pos()

    def mouseMoveEvent(self, mouse_event):
        super().mouseMoveEvent(mouse_event)

        new_mouse_pos = mouse_event.pos()
        new_mouse_in_world = new_mouse_pos * self.inverse_world_transform()
        last_mouse_in_world = self._last_mouse_pos * self.inverse_world_transform()

        dx = new_mouse_in_world.x() - last_mouse_in_world.x()
        dy = new_mouse_in_world.y() - last_mouse_in_world.y()
        self.translate(dx, dy)

        self._last_mouse_pos = new_mouse_pos
