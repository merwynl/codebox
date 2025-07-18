
'''

PYQT5 - Labels

'''


# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
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


        # Labels
        label = QLabel("Hello", self)
        label.setFont(QFont("Consolas", 18))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color: #F0F0F0;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            )

        label.setAlignment(Qt.AlignTop)  # Vertical Top
        label.setAlignment(Qt.AlignBottom)  # Vertical Bottom
        label.setAlignment(Qt.AlignVCenter)  # Verticle center

        label.setAlignment(Qt.AlignLeft)  # Horizontal Left
        label.setAlignment(Qt.AlignRight)  # Horizontal Right
        label.setAlignment(Qt.AlignHCenter) # Horizontal Center
        label.setAlignment(Qt.AlignCenter) # Abs Center

        # Using Or | operand to combine multiple alignment
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # Center & Bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # Verticle & Horizontal Center

def main():
    # Main constructor windows & showing the window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

# If we're running this file directly, call the main function.
if __name__ == '__main__':
    main()
