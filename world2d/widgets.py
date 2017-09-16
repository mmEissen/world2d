
from PyQt5.QtCore import QPoint, QPointF
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
        """Returns the inverted world_transform.
        """
        inverted, _ = self.world_transform.inverted()
        return inverted

    def world_painter(self, painter_class=QPainter):
        """Create a painter with the world transformation.

        Args:
            painter_class: You may specify a different class for the painter to be created. This
                should be a subclass of QPainter. Default is QPainter.
        """
        painter = painter_class()
        painter.begin(self)
        painter.setWorldMatrixEnabled(True)
        painter.setWorldTransform(self.world_transform)
        return painter

    def translate(self, dx, dy):
        """Translate the viewport.
        """
        self.world_transform.translate(dx, dy)
        self.update()

    def zoom(self, amount, center):
        """Scale the viewport around a center point.
        """
        self.world_transform.translate(center.x(), center.y())
        self.world_transform.scale(amount, amount)
        self.world_transform.translate(-center.x(), -center.y())
        self.update()

    def zoom_to_fit(self, bounding_box):
        """Set the scale to fit the bounding_box and center on it.
        """
        scale_x = self.width() / bounding_box.width()
        scale_y = self.height() / bounding_box.height()
        scale = min(scale_x, scale_y)

        dx = bounding_box.center().x()
        dy = bounding_box.center().y()

        self.world_transform = QTransform()
        self.world_transform.translate(self.width() / 2, self.height() / 2)
        self.world_transform.scale(scale, scale)
        self.world_transform.translate(-dx, -dy)
        self.update()

    def wheelEvent(self, wheel_event):
        super().wheelEvent(wheel_event)
        zoom_amount = self.zoom_base ** wheel_event.angleDelta().y()
        center = QPointF(wheel_event.pos()) * self.inverse_world_transform()
        self.zoom(zoom_amount, center)

    def mousePressEvent(self, mouse_event):
        super().mousePressEvent(mouse_event)
        self._last_mouse_pos = mouse_event.pos()

    def mouseMoveEvent(self, mouse_event):
        super().mouseMoveEvent(mouse_event)

        new_mouse_pos = mouse_event.pos()
        new_mouse_in_world = QPointF(new_mouse_pos) * self.inverse_world_transform()
        last_mouse_in_world = QPointF(self._last_mouse_pos) * self.inverse_world_transform()

        dx = new_mouse_in_world.x() - last_mouse_in_world.x()
        dy = new_mouse_in_world.y() - last_mouse_in_world.y()
        self.translate(dx, dy)

        self._last_mouse_pos = new_mouse_pos
