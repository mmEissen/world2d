
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRectF

from world2d.widgets import World2D


class ExampleWorld(World2D):

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = self.world_painter()
        painter.drawRect(-100, -100, 200, 200)
        painter.end()


def main():
    app = QApplication(sys.argv)

    w = ExampleWorld()
    w.resize(800, 600)
    w.move(100, 100)
    w.zoom_to_fit(QRectF(-100, -100, 200, 200))
    w.setWindowTitle('World2D Example')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
