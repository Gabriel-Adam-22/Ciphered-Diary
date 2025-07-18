from LogIn_SignIn_Window import LogIn_SignIn
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
import sys




def Login_window():
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    window = LogIn_SignIn()
    window.show()
    app.exec()
    return window


LogIn_SignIn_Window = Login_window()

if LogIn_SignIn_Window.LoginGranted():
    print(True)