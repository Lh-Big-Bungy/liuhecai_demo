import sys
import jwt
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Token Limited Application")
        self.setGeometry(100, 100, 800, 600)

        # 检查Token有效性
        if not self.is_token_valid():
            QMessageBox.warning(self, "Token Expired", "您的Token已经过期，无法继续使用该应用程序。")
            sys.exit()

    def is_token_valid(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE3OTE5ODl9.d2nk9d5tltU0mkFzecsVW__MYtcTd4i2CYElWD0aLt0"  # 在实际应用中，从配置文件或输入获取Token
        secret_key = 'lhhsa_youareinmyheart'
        try:
            jwt.decode(token, secret_key, algorithms=['HS256'])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
