import sys
from UI.liuhecai import Ui_MainWindow
from controls.textedit_restricted import TextEditRestrict
from controls.textbrowser_format import TextBrowserFormat
from controls.time_display import TimeDisplay
from controls.ball_button_click import ButtonClick
from controls.left_table import LeftTable
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QSizePolicy, QHeaderView
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
        # 设置 Size Policy 以使 tableWidget 随窗口大小变化
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 设置列宽自动调整
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
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
        self.clear_textbrowser.clicked.connect(self.ball_button_click.clear_textbrowser_input)  # 清空textbrowser的输入
        self.commit.clicked.connect(self.ball_button_click.copy_text_to_browser)  # 复制textedit的内容至textBrowser

        # 颜色
        self.red.clicked.connect(self.ball_button_click.red_on_button_clicked)  # 连接按钮的 clicked 信号到槽函数
        self.green.clicked.connect(self.ball_button_click.green_on_button_clicked)
        self.blue.clicked.connect(self.ball_button_click.blue_on_button_clicked)

        # 生肖
        self.mouse.clicked.connect(self.ball_button_click.mouse_on_button_clicked)
        self.bull.clicked.connect(self.ball_button_click.bull_on_button_clicked)
        self.tiger.clicked.connect(self.ball_button_click.tiger_on_button_clicked)
        self.rabbit.clicked.connect(self.ball_button_click.rabbit_on_button_clicked)
        self.dragon.clicked.connect(self.ball_button_click.dragon_on_button_clicked)
        self.snake.clicked.connect(self.ball_button_click.snake_on_button_clicked)
        self.horse.clicked.connect(self.ball_button_click.horse_on_button_clicked)
        self.goat.clicked.connect(self.ball_button_click.goat_on_button_clicked)
        self.monkey.clicked.connect(self.ball_button_click.monkey_on_button_clicked)
        self.chicken.clicked.connect(self.ball_button_click.chicken_on_button_clicked)
        self.dog.clicked.connect(self.ball_button_click.dog_on_button_clicked)
        self.pig.clicked.connect(self.ball_button_click.pig_on_button_clicked)

        # 颜色单双
        self.red_single.clicked.connect(self.ball_button_click.red_single_on_button_clicked)
        self.red_even.clicked.connect(self.ball_button_click.red_even_on_button_clicked)
        self.green_single.clicked.connect(self.ball_button_click.green_single_on_button_clicked)
        self.green_even.clicked.connect(self.ball_button_click.green_even_on_button_clicked)
        self.blue_single.clicked.connect(self.ball_button_click.blue_single_on_button_clicked)
        self.blue_even.clicked.connect(self.ball_button_click.blue_even_on_button_clicked)

        # 单双
        self.single.clicked.connect(self.ball_button_click.single_on_button_clicked)
        self.composite_single.clicked.connect(self.ball_button_click.composite_single_on_button_clicked)
        self.even.clicked.connect(self.ball_button_click.even_on_button_clicked)
        self.composite_even.clicked.connect(self.ball_button_click.composite_even_on_button_clicked)

        # 大小
        self.large.clicked.connect(self.ball_button_click.large_on_button_clicked)
        self.minor.clicked.connect(self.ball_button_click.minor_on_button_clicked)

        # 金木水火土
        self.gold.clicked.connect(self.ball_button_click.gold_on_button_clicked)
        self.wood.clicked.connect(self.ball_button_click.wood_on_button_clicked)
        self.water.clicked.connect(self.ball_button_click.water_on_button_clicked)
        self.fire.clicked.connect(self.ball_button_click.fire_on_button_clicked)
        self.soil.clicked.connect(self.ball_button_click.soil_on_button_clicked)

        # 尾大、尾小
        self.tail_large.clicked.connect(self.ball_button_click.tail_large_on_button_clicked)
        self.tail_minor.clicked.connect(self.ball_button_click.tail_minor_on_button_clicked)

        # 连号录入
        seq_input = SeqInput(self.seq_input, self.restricted_textedit)
        self.commit_two.clicked.connect(lambda: seq_input.data_processing())

        # 按键弹窗
        num_edit = NumberEdit()
        self.number_edit.clicked.connect(lambda: num_edit.show_dialog())  # lambda 只有在点击时才会触发
        loss_analysis = LossAnalysis()
        self.analysis_report.clicked.connect(lambda: loss_analysis.show_form(self.textBrowser.toPlainText()))

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