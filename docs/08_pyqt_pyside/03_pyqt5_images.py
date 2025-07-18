
'''

PYQT5 - Images
https://stackoverflow.com/questions/10307860/what-is-the-difference-between-qimage-and-qpixmap

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt # Used for alignemnts




# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set initial window properties & styling
        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))
        self.setStyleSheet("background-color: #282828;")

        # Image
        label = QLabel(self)
        label.setGeometry(0, 50, 32, 32)

        pixmap = QPixmap("ico/logo.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True) # Scale & stretch an image to fit the label.

        # Sets an image to the bottom right corner of a window.
        label.setGeometry(self.width()-label.width(),
                          self.height()-label.height(),
                          label.width(),
                          label.height()
                          )

        # Sets an image to the bottom left corner of a window.
        label.setGeometry(0,
                          self.height() - label.height(),
                          label.width(),
                          label.height()
                          )

        # Sets an image to the bottom center of a window.
        label.setGeometry((self.width()-label.width() )//2,
                          self.height() - label.height(),
                          label.width(),
                          label.height()
                          )

        # Sets an image to the top center of a window.
        label.setGeometry((self.width()-label.width() )//2,
                          0,
                          label.width(),
                          label.height()
                          )

        # Sets an image to the abs center of a window.
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height()
                          )



def main():
    # Main constructor windows & showing the window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

# If we're running this file directly, call the main function.
if __name__ == '__main__':
    main()
