
'''

PYQT5 - Line Edits

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))

        # Adding a line edit widget to the window
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.InitUI()

    def InitUI(self):

        self.line_edit.setGeometry(10, 10, 200, 30)

        # Applying a stylesheet to an entire category of items rather than individually.
        self.setStyleSheet("QLineEdit{"
                           "font-size: 12px;"
                           "font-family: Verdana;"
                           "padding: 5px"
                           "background-color: #383838;"
                           "}")
        self.line_edit.setPlaceholderText("Enter your name: ")

        self.button.setGeometry(220, 10, 100, 30)
        self.setStyleSheet("QPushButton{"
                           "font-size: 12px;"
                           "font-family: Verdana;"
                           "background-color: #383838;"
                           "}")

        # Connecting a signal(clicked) for the button to the slot(submit)
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text() # Getting a string from the line_edit
        print(f"Hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()