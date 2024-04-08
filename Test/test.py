import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from test1 import TimeDisplay
from UI.liuhecai import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 假设你已经在 Qt Designer 中给 QLabel 设置了一个 objectName，例如 "timeLabel"
        self.time_label = self.findChild(QLabel, "time_date_label")
        self.time_display = TimeDisplay(self.time_label)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()