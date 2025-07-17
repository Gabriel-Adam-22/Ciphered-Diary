from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
from Hash import txt_to_hash
import sys
import sqlite3

class Login(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(550, 300, 450, 200)

        self.db_name = "Ciphered_Diary.db"

        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        self.username_label = QLabel("Username : ", self)
        self.password_label = QLabel("Password : ", self)

        self.username_LineEdit = QLineEdit("", self)
        self.password_LineEdit = QLineEdit("", self)

        self._UI()

        self.Create_DB()
        
        if self.DB_is_empty() == []:
            self._signIn_UI()

        else:
            self._login_UI()

    # Data Base management
    def Create_DB(self):
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS User (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def DB_is_empty(self):
        self.c.execute("SELECT * FROM User")
        content = self.c.fetchall()

        return content

    # Check identifier
    def Check_user_info(self, given_username, given_password):
        self.c.execute("SELECT * FROM User")
        self.connectionInfo = self.c.fetchall()[0]

        registered_username = self.connectionInfo[0]
        registered_password = self.connectionInfo[1]

        if txt_to_hash(given_username) == registered_username and txt_to_hash(given_password) == registered_password:
            return True
        else:
            False

    def new_user(self, username, password):
        if len(username) > 0 and len(password) > 0:
            username = txt_to_hash(username)
            password = txt_to_hash(password)
            self.c.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, password,))
            self.conn.commit()
            self.close()

    # Set Main UI
    def _UI(self):
        self.username_label.setGeometry(50, 50, 1, 1)
        self.username_label.setFont(QFont("Consolas", 15))        
        self.username_label.adjustSize()

        self.password_label.setGeometry(50, 100, 1, 1)
        self.password_label.setFont(QFont("Consolas", 15))        
        self.password_label.adjustSize()

        self.username_LineEdit.setGeometry(160, 53, 250, 20)

        self.password_LineEdit.setGeometry(160, 103, 250, 20)
        self.password_LineEdit.setEchoMode(QLineEdit.EchoMode.Password)

    # Set Login or SignIn UI
    def _login_UI(self):
        self.setWindowTitle("Login")

        self.login_verify_button = QPushButton("Login", self)

        self.login_verify_button.setGeometry(190, 150, 1, 1)
        self.login_verify_button.adjustSize()

        self.login_verify_button.clicked.connect(lambda : print(self.Check_user_info(self.username_LineEdit.text(), self.password_LineEdit.text())))

    def _signIn_UI(self):
        self.setWindowTitle("Sign In")

        self.signIn_verify_button = QPushButton("Sign In", self)

        self.signIn_verify_button.setGeometry(190, 150, 1, 1)
        self.signIn_verify_button.adjustSize()

        self.signIn_verify_button.clicked.connect(lambda : self.new_user(self.username_LineEdit.text(), self.password_LineEdit.text()))


