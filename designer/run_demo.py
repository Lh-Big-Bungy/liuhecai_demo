import sys
from UI.liuhecai import Ui_MainWindow
from controls.textedit_restricted import TextEditRestrict
from controls.textbrowser_format import TextBrowserFormat
from controls.time_display import TimeDisplay
from controls.ball_button_click import ButtonClick
from controls.left_table import LeftTable
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit
from sql.sql_control import SqlControl
from controls.number_edit import NumberEdit


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 导入展示时间函数，并在此先找到控件label，然后调用函数
        self.time_label = self.findChild(QLabel, "time_date_label")
        self.date_2 = self.findChild(QLabel, "label_2")
        self.time_display = TimeDisplay(self.time_label, self.date_2)
        self.text_browser = TextBrowserFormat(self.textBrowser)
        # 左侧table，控制输入只能是整数
        self.table_view = LeftTable(self.tableWidget, self.textBrowser)
        self.table_commit.clicked.connect(self.table_view.copy_table_to_browser)  # 表格提交键
        self.clear.clicked.connect(self.table_view.clear_column_data)

        # textedit限制只能输入整数
        # 查找现有的QTextEdit控件
        self.original_textedit = self.findChild(QTextEdit, 'textEdit')
        # 创建TextEditRestrict实例
        self.restricted_textedit = TextEditRestrict()
        # 将TextEditRestrict添加到与原始QTextEdit相同的布局和位置
        self.original_textedit.parent().layout().replaceWidget(self.original_textedit, self.restricted_textedit)
        self.original_textedit.deleteLater()  # 删除原始控件

        # 按键录入
        self.ball_button_click = ButtonClick(self.restricted_textedit, self.textBrowser)
        self.commit.clicked.connect(self.ball_button_click.copy_text_to_browser)  # 复制textedit的内容至textBrowser
        self.red.clicked.connect(self.ball_button_click.red_on_button_clicked)  # 连接按钮的 clicked 信号到槽函数
        self.green.clicked.connect(self.ball_button_click.green_on_button_clicked)
        self.blue.clicked.connect(self.ball_button_click.blue_on_button_clicked)

        # 按键弹窗
        num_eidt = NumberEdit()
        self.number_edit.clicked.connect(lambda: num_eidt.show_dialog())

        # sql更改与插入
        # self.sql_control = SqlControl()
        # self.number_edit.clicked.connect(lambda: self.sql_control.query_database(self))  # 只有在点击时才会触发




if __name__ == '__main__':

    app = QApplication(sys.argv)

    # 创建对象
    mainWindow = MyWindow()
    # 显示
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
