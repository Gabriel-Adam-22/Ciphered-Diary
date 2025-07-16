from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
from Hash import txt_to_hash
import sys
import sqlite3

class Login(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(550, 300, 450, 200)
        self.setWindowTitle("Login")

        self.db_name = "Ciphered_Diary.db"

        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        self._Create_DB()
        
        if self._DB_is_empty() == []:
            self.signIn_UI()

        else:
            self.login_UI()


    def _Create_DB(self):
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS User (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def _DB_is_empty(self):
        self.c.execute("SELECT * FROM User")
        content = self.c.fetchall()

        return content

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
        pass

    def login_UI(self):
                
        self.login_username_label = QLabel("username : ", self)
        self.login_password_label = QLabel("Password : ", self)

        self.login_username_LineEdit = QLineEdit("", self)
        self.login_password_LineEdit = QLineEdit("", self)

        self.login_verify_button = QPushButton("Login", self)


        self.login_username_label.setGeometry(50, 50, 1, 1)
        self.login_username_label.setFont(QFont("Consolas", 15))        
        self.login_username_label.adjustSize()

        self.login_password_label.setGeometry(50, 100, 1, 1)
        self.login_password_label.setFont(QFont("Consolas", 15))        
        self.login_password_label.adjustSize()

        self.login_username_LineEdit.setGeometry(140, 53, 270, 20)

        self.login_password_LineEdit.setGeometry(160, 103, 250, 20)
        self.login_password_LineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_verify_button.setGeometry(190, 150, 1, 1)
        self.login_verify_button.adjustSize()

    def signIn_UI(self):

        self.setWindowTitle("Sign In")
                
        self.signIn_username_label = QLabel("username : ", self)
        self.signIn_password_label = QLabel("Password : ", self)

        self.signIn_username_LineEdit = QLineEdit("", self)
        self.signIn_password_LineEdit = QLineEdit("", self)

        self.signIn_username_LineEdit.setPlaceholderText("Set username ...")
        self.signIn_password_LineEdit.setPlaceholderText("Set password ...")

        self.signIn_verify_button = QPushButton("Sign In", self)

        self.signIn_username_label.setGeometry(50, 50, 1, 1)
        self.signIn_username_label.setFont(QFont("Consolas", 15))        
        self.signIn_username_label.adjustSize()

        self.signIn_password_label.setGeometry(50, 100, 1, 1)
        self.signIn_password_label.setFont(QFont("Consolas", 15))        
        self.signIn_password_label.adjustSize()
        
        self.signIn_username_LineEdit.setGeometry(140, 53, 270, 20)

        self.signIn_password_LineEdit.setGeometry(160, 103, 250, 20)
        self.signIn_password_LineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.signIn_verify_button.setGeometry(190, 150, 1, 1)
        self.signIn_verify_button.adjustSize()


def main():
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")

    window = Login()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()