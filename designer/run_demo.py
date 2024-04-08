import sys
from UI.liuhecai import Ui_MainWindow
from controls.chinese_restricted_textEdit import ChineseRestrictedTextEdit
from controls.time_display import TimeDisplay
from controls.button_click import Button_click
from controls.left_table import Left_table
#from Test.test1 import TimeDisplay
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 导入展示时间函数，并在此先找到控件label，然后调用函数
        self.time_label = self.findChild(QLabel, "time_date_label")
        self.date_2 = self.findChild(QLabel, "label_2")
        self.time_display = TimeDisplay(self.time_label, self.date_2)
        # 左侧table，控制输入只能是整数
        self.table_view = Left_table(self.tableWidget)
        # textedit限制只能输入整数
        # 查找现有的QTextEdit控件
        self.original_textedit = self.findChild(QTextEdit, 'textEdit')

        # 创建ChineseRestrictedTextEdit实例
        self.restricted_textedit = ChineseRestrictedTextEdit()

        # 将ChineseRestrictedTextEdit添加到与原始QTextEdit相同的布局和位置
        self.original_textedit.parent().layout().replaceWidget(self.original_textedit, self.restricted_textedit)
        self.original_textedit.deleteLater()  # 删除原始控件
        self.commit.clicked.connect(self.copy_text_to_browser)
        # 按键录入
        self.button_click = Button_click(self.restricted_textedit)
        self.red.clicked.connect(self.button_click.red_on_button_clicked)  # 连接按钮的 clicked 信号到槽函数
        self.green.clicked.connect(self.button_click.green_on_button_clicked)
        self.blue.clicked.connect(self.button_click.blue_on_button_clicked)

    def copy_text_to_browser(self):
        # 从第一个 QTextEdit 读取内容
        text = self.restricted_textedit.toPlainText()
        # 将内容设置到第二个 QTextEdit
        self.textBrowser.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # 创建对象
    mainWindow = MyWindow()
    # 显示
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
