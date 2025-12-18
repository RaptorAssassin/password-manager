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
    QMessageBox,
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
#TODO: passwords should be saved in a file
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
            global password_dialog
            self.list_widget.itemClicked.connect(self.show_password(name))

    #show the password dialog
    def show_password(self, name):
        password_dialog = PasswordDialog()
        password_dialog.show_password(name)


#handles master password popup
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__() 

        #window options
        self.setWindowTitle("Enter Master Password")
        self.resize(400, 50)
        self.setFixedSize(self.size())

        #create layout, master password input and submit button
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) #hides the password
        self.password_input.setPlaceholderText("Password")
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


class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()

        #window options
        self.setWindowTitle("Password")
        self.resize(400,50)
        self.setFixedSize(self.size())

        #create layout, add input to copy the password 
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.copy_button = QPushButton("Copy Password")
        self.copy_button.clicked.connect(self.copy_password(self.decrypted_password))
        self.delete_button = QPushButton("Delete Password")
        self.delete_button.clicked.connect(self.delete_password(password_name))
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.password_display)
        self.main_layout.addWidget(self.copy_button)
        self.main_layout.addWidget(self.delete_button)

        #password stuff
        self.password_name = ""
        self.encrypted_password = ""
        self.decrypted_password = ""

    def show_password(self, password):
        name = password
        if name in passwords:
            self.encrypted_password = passwords[name]
            self.decrypted_password = Encryption.decrypt(master_password_input)
            self.password_display.setText(self.decrypted_password)
            global password_name
            password_name = name
            self.show()
            print(f"showing password popup with password from {password_name}")

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.decrypted_password)
        self.copy_button.setText("Copied")
        print("copied password to clipboard")

    def delete_password(self, password):
        pass
        print("deleted password")
        

#handles encryption and decryption of passwords
class Encryption:
    def __init__(self):
        return
    
    def encrypt(self, password):
        pass

    def decrypt(self, password):
        pass

#handles storing of passwords
class Storage:
    def __init__(self):
        pass

        
#main loop
def main():

    #variables
    password_name = str

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
    password_dialog = PasswordDialog()
    running = True
    while running:
        pass
        
if __name__ == "__main__":
    main()
    