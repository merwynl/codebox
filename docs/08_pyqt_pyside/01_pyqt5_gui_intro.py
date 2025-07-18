
'''

PYQT5 - Gui Intro

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set initial window properties. setGeometry takes in screenspace position, width & height.
        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))

def main():
    # Main constructor windows. Default QT behaviour is to hide the window.
    app = QApplication(sys.argv) # Allows PyQT to pass in cmd arguments when running the py file from a terminal.
    window = MainWindow()
    window.show()

    sys.exit(app.exec_()) # Ensures a clean exit of our program. Waits for user input.

# If we're running this file directly, call the main function.
if __name__ == '__main__':
    main()