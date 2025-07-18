
'''

PYQT5 - Checkboxes
'''



# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))

        self.checkbox = QCheckBox("Checkbox 1", self)

        self.InitUI()

    def InitUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 16px; font-family: Consolas")

        # Sets the default state of a checkbox
        self.checkbox.setChecked(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()