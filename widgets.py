
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QTransform

class World2D(QWidget):
    """A Widget which has it's own 2D world space, onto which shapes can be drawn.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
