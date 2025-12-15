import sys
import json
import asyncio
from pathlib import Path
from PyQt6.QtWidgets import ( 
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QListWidget,
    QLineEdit,
    QDialog
    )
from PyQt6.QtGui import (
    QIcon,
)

#stores all saved passwords
passwords = {

}


#def new_password():

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Password Manager")
        self.setWindowIcon(app_icon_object)
        self.resize(640, 360)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

    #def center_window(window_instance) ->int:        
        
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Enter Master Password")
        self.resize(300, 200)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) #hides the password
        self.enter_button = QPushButton("Enter")

    def show(self):
        self.result = self.exec()
        self.show()        

    def get_password(self):

        return

class Encryption:
    def __init__(self):
        return
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    script_path = Path(__file__)
    script_dir = script_path.parent
    app_icon_path = script_dir / "images" / "icon.svg"
    app_icon_object = QIcon(str(app_icon_path))
    main_window = MainWindow()
    main_window.show()
    login_dialog = LoginDialog()
    login_dialog.show()

    entered_master_password = login_dialog.get_password()
