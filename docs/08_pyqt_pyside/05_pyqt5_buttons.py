
'''

PYQT5 - Buttons

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Good practice to keep class variables that you need on initalise within the constructor.
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Welcome", self)

        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))

        self.InitUI()

    def InitUI(self):

        self.button.setGeometry(150,100, 200, 100)
        self.button.setStyleSheet("font-size: 16px;")

        # Connecting a signal to a slot, then triggering a function. Signal representing some kind of key/mouse action.
        # Slot representing some kind of function or command.
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,200,200,100)
        self.label.setStyleSheet("font-size: 16px")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setFont(QFont("Verdana", 18))

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True) # Disable the ability to click a button
        self.label.setText("This is Codebox!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()