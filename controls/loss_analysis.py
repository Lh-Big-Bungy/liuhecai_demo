from UI.loss_analysis import Ui_Form
from PyQt5.QtWidgets import QWidget, QTableView, QHeaderView, QMessageBox, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QColor, QFont
from PyQt5.QtCore import Qt
from sql.data_write_to_sql import DataToSql
from service.data_analysis import DataAnalysis
import sqlite3

class LossAnalysis(QWidget, Ui_Form):
    def __init__(self, text_browser):
        super().__init__()
        self.text_browser = text_browser
        self.setupUi(self)
        self.setWindowTitle("数据分析界面")
        self.data_analysis = DataAnalysis
        self.money_summary = 0
        # 创建一个整数验证器
        int_validator = QIntValidator()
        # 设置验证器为lineEdit的验证器
        self.lineEdit.setValidator(int_validator)
        # 提交倍数与预亏损值
        self.pushButton.clicked.connect(lambda: self.commit_multiple_loss())
        self.data_del.clicked.connect(lambda: self.data_clear())
    def set_money_summary(self):
        try:
            # 连接到数据库
            connection = sqlite3.connect('sql/official_data.db')
            cursor = connection.cursor()
            # 执行SQL查询，筛选出num等于指定值的行
            cursor.execute("SELECT * FROM official_data_table")

            # 获取所有结果
            result = cursor.fetchall()
            print('---', result)
            self.money_summary = 0
            for i in result:
                self.money_summary += i[2]
            print(self.money_summary)
            # 关闭连接
            cursor.close()
            connection.close()
        except Exception as e:
            print("查询分析详情出错:", e)
        self.label.setText('投注总金额为：<span style="font-weight:bold; color:red; font-size:18px;">{}</span>'.format(self.money_summary))
        self.total_money.setText(
            f'投注总金额为：<span style="font-weight:bold; color:red; font-size:18px;">{self.money_summary}</span>')


    def get_data_from_sql(self, num):
        try:
            # 连接到数据库
            connection = sqlite3.connect('sql/official_data.db')
            cursor = connection.cursor()
            # 执行SQL查询，筛选出num等于指定值的行
            cursor.execute("SELECT * FROM catch_and_throw_table WHERE num = ?", (num,))

            # 获取所有结果
            result = cursor.fetchall()
            if result:
                self.num = result[0][1]
                self.total = result[0][2]
                self.throw = result[0][3]
                self.catch = result[0][4]
            else:
                self.num = num
                self.total = 0
                self.throw = 0
                self.catch = 0
            # 关闭连接
            cursor.close()
            connection.close()
        except Exception as e:
            print("查询分析详情出错:", e)


    def table_view(self):

        # 创建数据模型
        model = QStandardItemModel()
        # 创建表格视图并设置数据模型
        table_view = self.tableView
        table_view.setModel(model)
        # 设置列数和表头
        model.setColumnCount(12)
        headers = ["码号", "总金额", "应抛数", "留下数", "码号", "总金额", "应抛数", "留下数",
                                         "码号", "总金额", "应抛数", "留下数"]
        # 定义颜色
        orange = QColor(255, 165, 0)
        blue = QColor(173, 216, 230)
        yellow = QColor(255, 255, 224)
        green = QColor(144, 238, 144)
        red = QColor(255, 0, 0)
        # 设置字体加粗
        bold_font = QFont()
        bold_font.setBold(True)
        # 设置表头
        for i, header in enumerate(headers):
            item = QStandardItem(header)
            if header == "应抛数":
                item.setForeground(red)  # 设置“应抛数”列的表头字体颜色为红色
                item.setFont(bold_font)  # 设置“应抛数”列的表头字体加粗
            model.setHorizontalHeaderItem(i, item)

        # 添加数据
        re_row = 0
        for row in range(0, 49):
            row_num = str(row+1).zfill(2)  # 自动补全为两位数字，小于10时，自动在前面加0，例01、09
            self.get_data_from_sql(row_num)
            if row < 17:
                item_name = QStandardItem(row_num)
                item_name.setBackground(orange)  # 设置“码号”列的背景颜色为橙色
                model.setItem(row, 0, item_name)  # 在第一列添加项目
                total_item = QStandardItem(str(self.total))
                throw_item = QStandardItem(str(self.throw))
                catch_item = QStandardItem(str(self.catch))
                total_item.setBackground(blue)
                throw_item.setBackground(yellow)
                throw_item.setForeground(red)  # 设置“应抛数”列的字体颜色为红色
                throw_item.setFont(bold_font)  # 设置“应抛数”列的字体加粗
                catch_item.setBackground(green)
                model.setItem(row, 1, total_item)
                model.setItem(row, 2, throw_item)
                model.setItem(row, 3, catch_item)
            elif row < 34:
                item_name = QStandardItem(row_num)
                item_name.setBackground(orange)  # 设置“码号”列的背景颜色为橙色
                model.setItem(re_row, 4, item_name)  # 在第五列添加项目
                total_item = QStandardItem(str(self.total))
                throw_item = QStandardItem(str(self.throw))
                catch_item = QStandardItem(str(self.catch))
                total_item.setBackground(blue)
                throw_item.setBackground(yellow)
                throw_item.setForeground(red)  # 设置“应抛数”列的字体颜色为红色
                throw_item.setFont(bold_font)  # 设置“应抛数”列的字体加粗
                catch_item.setBackground(green)
                model.setItem(re_row, 5, total_item)
                model.setItem(re_row, 6, throw_item)
                model.setItem(re_row, 7, catch_item)
                re_row += 1
            else:
                if re_row >= 17:
                    re_row = 0
                item_name = QStandardItem(row_num)
                item_name.setBackground(orange)  # 设置“码号”列的背景颜色为橙色
                model.setItem(re_row, 8, item_name)  # 在第九列添加项目
                total_item = QStandardItem(str(self.total))
                throw_item = QStandardItem(str(self.throw))
                catch_item = QStandardItem(str(self.catch))
                total_item.setBackground(blue)
                throw_item.setBackground(yellow)
                throw_item.setForeground(red)  # 设置“应抛数”列的字体颜色为红色
                throw_item.setFont(bold_font)  # 设置“应抛数”列的字体加粗
                catch_item.setBackground(green)
                model.setItem(re_row, 9, total_item)
                model.setItem(re_row, 10, throw_item)
                model.setItem(re_row, 11, catch_item)
                re_row += 1

        # 设置整个表格只读
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        # 调整列宽以适应内容
        table_view.resizeColumnsToContents()
        # 隐藏左侧表头
        self.tableView.verticalHeader().setVisible(False)
        # 设置所有单元格内容居中
        self.tableView.setModel(model)
        self.tableView.setModel(model)
        for i in range(model.columnCount()):
            for j in range(model.rowCount()):
                index = model.index(j, i)
                self.tableView.model().setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)
        # 设置表头拉伸模式
        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # 调整行高以适应内容
        table_view.resizeRowsToContents()


    def commit_multiple_loss(self):
        if self.spinBox.value() and self.lineEdit.text():
            odds_loss_to_sql = DataToSql(odds=str(self.spinBox.value()), loss=int(self.lineEdit.text()))
            odds_loss_to_sql.odds_loss_to_database()
            self.set_money_summary()  # 重算总金额
            data_analysis = DataAnalysis()
            data_analysis.run()  # 进行数据分析，并写入数据库
            self.throw_up_money = self.money_summary - data_analysis.win_money
            # 显示总抛出数和总留下数
            self.total_throw_label.setText(
                f'总抛出数为：<span style="font-weight:bold; color:red; font-size:18px;">{self.throw_up_money}</span>')
            self.total_catch_label.setText(
                f'总留下数为：<span style="font-weight:bold; color:red; font-size:18px;">{data_analysis.win_money}</span>')
            # 需判断数据是否为空
            if data_analysis.num_money_dict:
                self.table_view()
                self.label_2.setText('最大预亏损金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
                '赔率为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
                '单个号码最大注数为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>元，'
                '吃进总金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
                '实际最大亏损金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>'.format(
                    data_analysis.base_loss, data_analysis.odds, data_analysis.max_num, data_analysis.win_money, data_analysis.actual_loss_amount))
            else:
                QMessageBox.warning(self, "错误", "数据为空，请重新输入数据")
            # 设置标签的大小策略
            self.label_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # 使标签内容换行
            self.label_2.setWordWrap(True)
            # 设置固定宽度，单位为像素，根据需要调整宽度值
            self.label_2.setFixedWidth(1000)
            # 调整标签大小以适应内容
            self.label_2.adjustSize()
            # 调整窗口大小以适应内容
            self.adjustSize()
        else:
            QMessageBox.warning(self, "错误", "赔率或预亏损为空")


    def data_clear(self):
        # 连接到数据库
        connection = sqlite3.connect('sql/official_data.db')
        cursor = connection.cursor()
        # 清空catch_and_throw_table、 official_data_table
        cursor.execute("DELETE FROM catch_and_throw_table")
        cursor.execute("DELETE FROM official_data_table")
        # 提交更改并关闭连接
        connection.commit()
        connection.close()
        self.set_money_summary()  # 重算总金额
        self.text_browser.clear()
        self.table_view()
        QMessageBox.warning(self, "警告", "数据已清除，若想继续进行数据分析，请重新输入数据")
        self.label_2.setText('<span style="font-weight:bold; color:red; font-size:18px;">数据已清除，若想继续进行数据分析，请重新输入数据</span>')
        # 设置标签的大小策略
        self.label_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 使标签内容换行
        self.label_2.setWordWrap(True)
        # 设置固定宽度，单位为像素，根据需要调整宽度值
        self.label_2.setFixedWidth(1000)
        # 调整标签大小以适应内容
        self.label_2.adjustSize()
    def show_form(self, data):
        if data:
            self.set_money_summary()
            self.show()
        else:
            QMessageBox.warning(self, "错误", "输入号码为空")
