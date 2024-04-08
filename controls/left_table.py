from PyQt5.QtWidgets import QTableWidgetItem, QStyledItemDelegate, QLineEdit, QApplication
from PyQt5.QtGui import QIntValidator, QPainter, QTextOption
from PyQt5.QtCore import Qt

class IntegerDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QIntValidator())
        return editor

class Left_table():
    def __init__(self, tableWidget):
        self.tableWidget = tableWidget
        self.table_view()  # 调用方法以设置表格
    def table_view(self):
        integer_delegate = IntegerDelegate(self.tableWidget)
        # 指定第二列只能输入整数
        self.tableWidget.setItemDelegateForColumn(1, integer_delegate)


        # 设置列数
        self.tableWidget.setColumnCount(2)
        # 表头标题列表
        headers = ["码号", "金额"]
        # 设置表头
        self.tableWidget.setHorizontalHeaderLabels(headers)
        # 插入行
        for row in range(0, 49):
            self.tableWidget.insertRow(row)
        for row in range(1, 50):
            # 第一列
            item = QTableWidgetItem(str(row).zfill(2))  # 使用 zfill 确保两位数格式
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 不可编辑
            item.setTextAlignment(Qt.AlignCenter)
            print(row)
            self.tableWidget.setItem(row-1, 0, item)

            # 第二列
            item2 = QTableWidgetItem('0')
            item2.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
            self.tableWidget.setItem(row-1, 1, item2)
