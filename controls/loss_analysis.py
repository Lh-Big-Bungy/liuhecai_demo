from UI.loss_analysis import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class LossAnalysis(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("数据分析界面")
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
        for row in range(5):
            item_name = QStandardItem(f"Person {row + 1}")
            item_age = QStandardItem(str(20 + row))
            model.appendRow([item_name, item_age])



        # 调整列宽以适应内容
        table_view.resizeColumnsToContents()

    def show_form(self):
        self.show()
        # form = LossAnalysis()
        # form.exec_()
