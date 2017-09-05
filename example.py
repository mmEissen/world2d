
import sys

from PyQt5.QtWidgets import QApplication

from widgets import World2D


class ExampleWorld(World2D):

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = self.world_painter()
        painter.drawRect(0, 0, 100, 100)
        painter.end()


def main():
    app = QApplication(sys.argv)

    w = ExampleWorld()
    w.resize(800, 600)
    w.move(100, 100)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
