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
from controls.log_in import LoginDialog
from controls.loss_analysis import LossAnalysis
from controls.sequential_input import SeqInput

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        # self.setWindowTitle("六合彩")
        # 导入展示时间函数，并在此先找到控件label，然后调用函数
        self.user_name.setText('欢迎，{}！'.format(username))
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

        # 连号录入
        seq_input = SeqInput(self.seq_input, self.restricted_textedit)
        self.commit_two.clicked.connect(lambda: seq_input.data_processing())

        # 按键弹窗
        num_edit = NumberEdit()
        self.number_edit.clicked.connect(lambda: num_edit.show_dialog())  # lambda 只有在点击时才会触发
        loss_analysis = LossAnalysis()
        self.analysis_report.clicked.connect(lambda: loss_analysis.show_form())

        # sql更改与插入
        # self.sql_control = SqlControl()
        # self.number_edit.clicked.connect(lambda: self.sql_control.query_database(self))  # 只有在点击时才会触发




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login_dialog = LoginDialog()
    # if login_dialog.exec_() == QDialog.Accepted:
    #     username = login_dialog.login()  # 获取登录成功的用户名
    #     main_window = MyWindow(username)
    #     main_window.show()  # 显示主界面
    #     # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    #     sys.exit(app.exec_())
    main_window = MyWindow('admin')
    main_window.show()  # 显示主界面
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())