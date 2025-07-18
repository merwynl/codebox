
'''

PYQT5 - Radio Buttons

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))

        # Calling the QRadioButton to create radio buttons
        self.radio1 = QRadioButton("Category A: Option 1", self)
        self.radio2 = QRadioButton("Category A: Option 2", self)
        self.radio3 = QRadioButton("Category A: Option 3", self)
        self.radio4 = QRadioButton("Category B: Option 4", self)
        self.radio5 = QRadioButton("Category B: Option 5", self)

        # Defining button groups
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.InitUI()

    def InitUI(self):

        # Applying transforms to radio buttons
        self.radio1.setGeometry(10,0, 300, 50)
        self.radio2.setGeometry(10, 35, 300, 50)
        self.radio3.setGeometry(10, 70, 300, 50)
        self.radio4.setGeometry(10, 105, 300, 50)
        self.radio5.setGeometry(10, 140, 300, 50)

        # Applying a stylesheet to an entire category of items rather than individually.
        self.setStyleSheet("QRadioButton{"
                           "font-size: 16px;"
                           "font-family: Verdana;"
                           "padding: 10px;"
                           "}")

        # Adding radio buttons to button groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connecting a signal(toggled) from the radio button to a slot(radio_button_changed)
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        selected_radio_button = self.sender() # Receives a signal
        if selected_radio_button.isChecked():
            print(f"{selected_radio_button.text()} has been selected.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()