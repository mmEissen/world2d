
import sys

from PyQt5.QtWidgets import QApplication

from widgets import World2D

def main():
    app = QApplication(sys.argv)

    w = World2D()
    w.resize(800, 600)
    w.move(100, 100)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
