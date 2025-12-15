import sys
from PyQt6.QtWidgets import ( 
    QApplication,
    QWidget,
    QLabel,
    QPushButton

    )
from PyQt6.QtGui import QScreen

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Password Manager")
window.setGeometry(100, 100, 400, 200)

label = QLabel("Hello, World", parent=window)
label.move(150, 90)

window.show()

sys.exit(app.exec())