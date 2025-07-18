
'''

PYQT5 - Checkboxes
'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
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
        self.checkbox.setStyleSheet("font-size: 16px; "
                                    "font-family: Verdana")

        # Sets the default state of a checkbox
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed) # Connects a signal(stateChanged) to a slot(method)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food!")
        else:
            print("You do not like food!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()