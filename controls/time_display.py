from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QTimer, QDateTime

class TimeDisplay:
    def __init__(self, label: QLabel, label_2):
        self.label = label
        self.label_2 =label_2
        self.timer = QTimer()
        # 注意：这里的 lambda 是为了保持原有 update_time 的签名，即使它不接受任何参数
        self.timer.timeout.connect(lambda: self.update_time())
        self.timer.start(1000)  # 每秒更新一次时间
    def update_time(self):
        # 获取当前时间，并格式化为字符串
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        # 更新 QLabel 的文本
        font = QFont("Arial", 12, QFont.Bold)  # 设置字体为 Arial，大小为 12，加粗
        color = QColor(255, 0, 0)  # 设置颜色为红色
        self.label_2.setFont(font)
        self.label.setStyleSheet("color: rgb({}, {}, {});".format(color.red(), color.green(), color.blue()))
        self.label.setFont(font)
        self.label.setText(current_time)