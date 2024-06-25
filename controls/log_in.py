import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from Token.token_verify import is_token_valid
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")

        layout = QVBoxLayout()

        self.token = QLineEdit()

        login_button = QPushButton("登录")
        login_button.clicked.connect(self.login)

        layout.addWidget(QLabel("Token:"))
        layout.addWidget(self.token)

        layout.addWidget(login_button)

        self.setLayout(layout)


    def login(self):
        token = self.token.text()
        if is_token_valid(token):
            self.accept()  # 关闭登录对话框并返回 Accepted 状态
        else:
            QMessageBox.warning(self, "Token Expired", "您的Token已经过期，无法继续使用该应用程序。")
            sys.exit()

