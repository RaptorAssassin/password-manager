import sys
import json
from pathlib import Path
from PyQt6.QtWidgets import ( 
    QApplication,
    QWidget,
    QLabel,
    QPushButton

    )
from PyQt6.QtGui import (
    QIcon
)

#stores all saved passwords
passwords = {

}


#def new_password():

class Window:
    def __init__(self):
        return
    #def center_window(window_instance) ->int:
        

class Encryption:
    def __init__(self):
        return
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    script_path = Path(__file__)
    script_dir = script_path.parent
    app_icon_path = script_dir / "images" / "icon.svg"
    app_icon_object = QIcon(str(app_icon_path))
    window = QWidget()
    window.setWindowTitle("Password Manager")
    window.setWindowIcon(app_icon_object)
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())