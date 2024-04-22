import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")

        layout = QVBoxLayout()

        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("登录")
        login_button.clicked.connect(self.login)

        register_button = QPushButton("注册")
        register_button.clicked.connect(self.register)

        layout.addWidget(QLabel("用户名:"))
        layout.addWidget(self.username_edit)
        layout.addWidget(QLabel("密码:"))
        layout.addWidget(self.password_edit)
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        self.setLayout(layout)

        # 连接到 SQLite 数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../sql/users.db')
        if not self.db.open():
            QMessageBox.critical(self, "错误", "无法连接到数据库")
            sys.exit(1)

        # 创建用户表
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE username = :username AND password = :password")
        query.bindValue(":username", username)
        query.bindValue(":password", password)
        if query.exec_() and query.next():
            self.accept()  # 关闭登录对话框并返回 Accepted 状态
            return username  # 返回用户名
        else:
            QMessageBox.warning(self, "错误", "用户名或密码错误")

    def register(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        query = QSqlQuery()
        query.prepare("INSERT INTO users (username, password) VALUES (:username, :password)")
        query.bindValue(":username", username)
        query.bindValue(":password", password)
        if query.exec_():
            QMessageBox.information(self, "成功", "注册成功")
        else:
            QMessageBox.warning(self, "错误", "注册失败")


