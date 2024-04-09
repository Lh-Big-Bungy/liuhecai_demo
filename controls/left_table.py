from PyQt5.QtWidgets import QTableWidgetItem, QStyledItemDelegate, QLineEdit, QApplication
from PyQt5.QtGui import QIntValidator, QPainter, QTextOption
from PyQt5.QtCore import Qt

class IntegerDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QIntValidator())
        return editor

class LeftTable():
    def __init__(self, tableWidget, textBrowser):
        self.tableWidget = tableWidget
        self.textBrowser = textBrowser
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
            self.tableWidget.setItem(row-1, 0, item)
            # 第二列
            item2 = QTableWidgetItem('0')
            item2.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
            self.tableWidget.setItem(row-1, 1, item2)

    def copy_table_to_browser(self):
        # 初始化一个字符串来保存表格内容
        table_content = ""
        # 遍历表格的每一行和每一列
        for row in range(self.tableWidget.rowCount()):
            flag = True
            for col in range(self.tableWidget.columnCount()):
                # 获取单元格的文本内容
                item = self.tableWidget.item(row, col)
                if col == 1 and item.text() == '0':
                    table_content = temp_content
                    flag = False
                if item:
                    cell_text = item.text()
                else:
                    cell_text = ""
                    # 将单元格内容添加到字符串中，并添加分隔符
                temp_content = table_content
                if flag:
                    table_content += cell_text + "\t"  # 使用制表符作为列分隔符
            if flag:
                table_content += '\n'
            else:
                pass


        self.textBrowser.setText(table_content)

    def clear_column_data(self):
        """
        清除指定列的数据。

        :param table_widget: QTableWidget 对象
        :param column_index: 要清除的列的索引
        """
        # 遍历指定列的所有行
        for row in range(self.tableWidget.rowCount()):
            # 获取当前行的指定列的单元格项
            item2 = QTableWidgetItem('0')
            item2.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
            self.tableWidget.setItem(row - 1, 1, item2)