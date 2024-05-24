from UI.loss_analysis import Ui_Form
from PyQt5.QtWidgets import QWidget, QTableView, QHeaderView, QMessageBox, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QColor
from PyQt5.QtCore import Qt
from sql.data_write_to_sql import DataToSql
from service.data_analysis import DataAnalysis
import sqlite3

class LossAnalysis(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("数据分析界面")
        self.data_analysis = DataAnalysis



        # 创建一个整数验证器
        int_validator = QIntValidator()
        # 设置验证器为lineEdit的验证器
        self.lineEdit.setValidator(int_validator)
        # 提交倍数与预亏损值
        self.pushButton.clicked.connect(lambda: self.commit_multiple_loss())

    def get_data_from_sql(self, num):
        try:
            # 连接到数据库
            connection = sqlite3.connect('../sql/catch_and_throw.db')
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
        model.setHorizontalHeaderLabels(["码号", "总金额", "应抛数", "留下数", "码号", "总金额", "应抛数", "留下数",
                                         "码号", "总金额", "应抛数", "留下数"])
        # 定义颜色
        orange = QColor(255, 165, 0)
        blue = QColor(173, 216, 230)
        yellow = QColor(255, 255, 224)
        green = QColor(144, 238, 144)

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
            data_analysis = DataAnalysis()
            data_analysis.run()  # 进行数据分析，并写入数据库
            self.table_view()
            self.label_2.setText('最大预亏损金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
            '赔率为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
            '单个号码最大注数为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>元，'
            '吃进总金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>，'
            '实际最大亏损金额为<span style="font-weight:bold; color:red; font-size:18px;">{}</span>'.format(
                data_analysis.base_loss, data_analysis.odds, data_analysis.max_num, data_analysis.win_money, data_analysis.actual_loss_amount))
            # 设置标签的大小策略
            self.label_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # 使标签内容换行
            self.label_2.setWordWrap(True)
            # 设置固定宽度，单位为像素，根据需要调整宽度值
            self.label_2.setFixedWidth(1000)
            # 调整标签大小以适应内容
            self.label_2.adjustSize()
        else:
            QMessageBox.warning(self, "错误", "赔率或预亏损为空")





    def show_form(self, data):
        if data:
            data_to_sql = DataToSql(data)
            data_to_sql.write_to_database()
            self.show()
        else:
            QMessageBox.warning(self, "错误", "输入号码为空")

