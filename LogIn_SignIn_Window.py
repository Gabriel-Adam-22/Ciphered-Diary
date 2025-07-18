from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from Hash import txt_to_hash
import sqlite3

class LogIn_SignIn(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(550, 300, 450, 200)

        self.db_name = "Ciphered_Diary.db"
        self.login_is_ok = False # Used to determine if the login was granted

        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        self.username_Label = QLabel("Username : ", self)
        self.password_Label = QLabel("Password : ", self)

        self.username_LineEdit = QLineEdit("", self)
        self.password_LineEdit = QLineEdit("", self)

        self._UI()

        self.Create_DB()
        
        if self.isDbEmpty() == []:  self._signIn_UI()

        else:  self._login_UI()

    # Data Base management
    def Create_DB(self):
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS User (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def isDbEmpty(self):
        self.c.execute("SELECT * FROM User")
        user_identifiers = self.c.fetchall()

        return user_identifiers

    # Check identifier
    def checkUserInfo(self, given_username, given_password):

        self.c.execute("SELECT * FROM User")
        self.identifiers = self.c.fetchall()[0]

        registered_username = self.identifiers[0]
        registered_password = self.identifiers[1]

        if txt_to_hash(given_username) == registered_username and txt_to_hash(given_password) == registered_password:
            self.login_is_ok = True
            self.close()
        else:
            self._Login_MessageboxError()

    def newUser(self, username, password):
        if len(username) > 0 and len(password) > 4:

            username = txt_to_hash(username)
            password = txt_to_hash(password)
            
            self.c.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, password,))
            self.conn.commit()

            self.login_is_ok = True

            self.close()
        
        else:
            self._Login_MessageboxError()

    # Set UI
    def _UI(self):
        self.username_Label.setGeometry(50, 50, 1, 1)
        self.username_Label.setFont(QFont("Consolas", 15))        
        self.username_Label.adjustSize()

        self.password_Label.setGeometry(50, 100, 1, 1)
        self.password_Label.setFont(QFont("Consolas", 15))        
        self.password_Label.adjustSize()

        self.username_LineEdit.setGeometry(160, 53, 250, 20)

        self.password_LineEdit.setGeometry(160, 103, 250, 20)
        self.password_LineEdit.setEchoMode(QLineEdit.EchoMode.Password)

    def _login_UI(self):
        self.setWindowTitle("Login")

        self.login_verify_button = QPushButton("Login", self)

        self.login_verify_button.setGeometry(190, 150, 1, 1)
        self.login_verify_button.adjustSize()

        self.login_verify_button.clicked.connect(lambda : self.checkUserInfo(self.username_LineEdit.text(), self.password_LineEdit.text()))

    def _signIn_UI(self):
        self.setWindowTitle("Sign In")

        self.signIn_verify_button = QPushButton("Sign In", self)

        self.signIn_verify_button.setGeometry(190, 150, 1, 1)
        self.signIn_verify_button.adjustSize()

        self.signIn_verify_button.clicked.connect(lambda : self.newUser(self.username_LineEdit.text(), self.password_LineEdit.text()))

    def _Login_MessageboxError(self):
        messagebox_error = QMessageBox()
        messagebox_error.setIcon(QMessageBox.Icon.Critical)
        messagebox_error.setWindowTitle("Error")
        messagebox_error.setText("The Username or Password is incorrect")
        messagebox_error.setStandardButtons(QMessageBox.StandardButton.Ok)
        messagebox_error.exec()

    # Use to determine if the login was granted
    def LoginGranted(self):
        return self.login_is_ok