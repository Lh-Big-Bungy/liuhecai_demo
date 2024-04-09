import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, \
    QTextBrowser
from PyQt5.QtGui import QFont


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 QTableWidget 控件并填充一些数据
        self.tableWidget = QTableWidget(4, 3, self)  # 4行3列
        self.tableWidget.setHorizontalHeaderLabels(['Header 1', 'Header 2', 'Header 3'])
        for row in range(4):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row},{col}")
                self.tableWidget.setItem(row, col, item)

                # 创建 QTextBrowser 控件
        self.textBrowser = QTextBrowser(self)

        # 创建一个按钮，用于触发数据复制操作
        self.button = QPushButton('Copy Table to Browser', self)
        self.button.clicked.connect(self.copy_table_to_browser)

        # 创建布局并添加控件
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('PyQt5 TableWidget to TextBrowser Example')
        self.setGeometry(300, 300, 500, 400)

        # 设置 QTextBrowser 的字符大小为 12
        self.set_text_browser_font_size(12)

    def set_text_browser_font_size(self, size):
        """
        设置 QTextBrowser 的字符大小。
        """
        font = QFont()
        font.setPointSize(size)
        self.textBrowser.setFont(font)

    def copy_table_to_browser(self):
        # 初始化一个字符串来保存表格内容
        table_content = ""

        # 遍历表格的每一行和每一列
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                # 获取单元格的文本内容
                item = self.tableWidget.item(row, col)
                if item:
                    cell_text = item.text()
                else:
                    cell_text = ""

                    # 将单元格内容添加到字符串中，并添加分隔符（例如制表符）
                table_content += cell_text + "\t"

                # 在每行末尾添加换行符
            table_content += "\n"

            # 将得到的字符串设置为 QTextBrowser 的内容
        self.textBrowser.setText(table_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())