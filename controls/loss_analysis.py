from UI.loss_analysis import Ui_Form
from PyQt5.QtWidgets import QWidget, QTableView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from PyQt5.QtCore import Qt

class LossAnalysis(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("数据分析界面")
        # 创建一个整数验证器
        int_validator = QIntValidator()
        # 设置验证器为lineEdit的验证器
        self.lineEdit.setValidator(int_validator)
        self.table_view()
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

        # 添加数据
        re_row = 0

        for row in range(0, 49):
            if row < 17:
                item_name = QStandardItem(f"{row + 1}")
                model.setItem(row, 0, item_name)  # 在第一列添加项目
            elif row < 34:
                item_name = QStandardItem(f"{row + 1}")
                model.setItem(re_row, 4, item_name)  # 在第一列添加项目
                re_row += 1
            else:
                if re_row >= 17:
                    re_row = 0
                item_name = QStandardItem(f"{row + 1}")
                model.setItem(re_row, 8, item_name)  # 在第一列添加项目
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


    def show_form(self):
        self.show()

