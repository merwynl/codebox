import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.move(450, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

# Display Logo
image = QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet("margin-top: 100px;")


#button widget
button = QPushButton("PLAY")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
    "border: 4px solid '#BC006c';" +
    "border-radius: 15px;" +
    "font-size: 35px;" +
    "color: 'white'"
)

grid.addWidget(logo, 0, 0)
grid.addWidget(button, 1, 0)

window.setLayout(grid)

window.show()
sys.exit(app.exec())