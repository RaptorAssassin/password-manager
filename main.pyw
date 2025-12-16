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
    QHBoxLayout,
    QLineEdit,
    QDialog,
    QAbstractItemView
    )
from PyQt6.QtGui import (
    QIcon,
)
from PyQt6.QtCore import (
    Qt,
    QPoint
)

#stores all saved, encrypted passwords
passwords = {
    "name": "password",
    "name2": "password2",
    "name3": "password3"
}
    

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #window actions
        self.setWindowTitle("Password Manager")
        self.resize(640, 360)

        #icon
        script_path = Path(__file__)
        script_dir = script_path.parent
        app_icon_path = script_dir / "images" / "icon.svg"
        app_icon_object = QIcon(str(app_icon_path))
        self.setWindowIcon(app_icon_object)
        
        #create main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #create list to display the passwords and add to the main layout
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
       
    #lists all passwords inside the main window
    def list_passwords(self):
        #clear the list
        self.list_widget.clear()
        #fill the list with the names of the passwords 
        for name in passwords.keys():
            item = QListWidgetItem(name)
            self.list_widget.addItem(item)


#handles master password popup
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Enter Master Password")
        self.resize(400, 50)
        self.setFixedSize(self.size())
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) #hides the password
        self.submit_button = QPushButton("Submit")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.password_input)
        self.input_layout.addWidget(self.submit_button)
        self.main_layout.addLayout(self.input_layout)
        global master_password_input
        master_password_input = self.password_input.text()
        self.submit_button.clicked.connect(self.accept_password) 

    #closes the master password popup
    def accept_password(self):
        global master_password_input
        master_password_input = self.password_input.text()
        if master_password_input != "":
            self.accept()


#handles encryption, decryption and storing of passwords
class Encryption:
    def __init__(self):
        return
    

#main loop
def main():
    app = QApplication(sys.argv)
    
    #create and show main password manager window
    main_window = MainWindow()
    main_window.show()
    
    #create and show dialog popup to enter master password
    login_dialog = LoginDialog()
    login_result = 0
    master_password_input = None
    while login_result == 0:
        login_dialog.show()
        login_result = login_dialog.exec()
    print(master_password_input)
    main_window.list_passwords()
    app.exec()
    
if __name__ == "__main__":
    main()
    