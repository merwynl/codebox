
'''

PYQT5 - Layouts

'''

# Import main QT Application & Main window module
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


# QT Applications require inheriting from the QMainWndow class.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set initial window properties & styling
        self.setWindowTitle("Codebox")
        self.setGeometry(1280,540,500,300)
        self.setWindowIcon(QIcon("ico/logo.png"))
        self.setStyleSheet("background-color: #282828;")

        self.initUI() # Initialise UI

    # Common practice to include an initUI function after the constructor to handle all UI layout.
    # Layouts can't be added to a window object. Windows have a specific design & structure.
    # Workflow: 1. Create a generic widget -> 2. Add a layout manager to widget -> 3. Add widget to the window.
    def initUI(self):

        # Create generic widget and add it to QMainWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Creating labels
        label_file = QLabel("File", self)
        label_edit = QLabel("Edit", self)
        label_create = QLabel("Create", self)
        label_browse = QLabel("Browse", self)
        label_help = QLabel("Help", self)

        # Setting some basic styling on the labels
        label_file.setStyleSheet("color: #F0F0F0; background-color: #383838;")
        label_edit.setStyleSheet("color: #F0F0F0; background-color: #383838;")
        label_create.setStyleSheet("color: #F0F0F0; background-color: #383838;")
        label_browse.setStyleSheet("color: #F0F0F0; background-color: #383838;")
        label_help.setStyleSheet("color: #F0F0F0; background-color: #383838;")

        # Applying a vertical layout for our labels. QHBoxLayout(), QVBoxLayout, QGridLayout
        grid = QGridLayout()

        # Adds out label widgets to the layout manager. Grid layouts require a row & column
        grid.addWidget(label_file, 0,0)
        grid.addWidget(label_edit, 0,1)
        grid.addWidget(label_create, 1,0)
        grid.addWidget(label_browse, 1,1)
        grid.addWidget(label_help, 1,2)

        # Applies our layout manager to the main widget
        central_widget.setLayout(grid)


def main():
    # Main constructor windows & showing the window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

# If we're running this file directly, call the main function.
if __name__ == '__main__':
    main()