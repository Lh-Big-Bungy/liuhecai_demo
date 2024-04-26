import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class SqlControl():
    def __init__(self):
        super().__init__()

        # 连接到 SQLite 数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('example.db')

    def query_database(self, parent_window):
        if not self.db.open():
            # QMessageBox.critical(None, "无法打开数据库", "无法连接到数据库")
            sys.exit(1)
        # 创建表
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

        # 插入一些示例数据
        # query.exec_("INSERT INTO people (name) VALUES ('Alice')")

        # 查询并输出数据
        query.exec_("SELECT * FROM people")
        result = ''
        while query.next():
            name = query.value(1)
            print(f"Name: {name}")
            result += name + '\n'
            # 显示查询结果
        QMessageBox.information(parent_window, "查询结果", result)

