from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
import datetime


class TimeDisplay:
    def __init__(self, label: QLabel):
        self.label = label
        self.timer = QTimer()
        # 注意：这里的 lambda 是为了保持原有 update_time 的签名，即使它不接受任何参数
        self.timer.timeout.connect(lambda: self.update_time())
        self.timer.start(1000)  # 每秒更新一次时间

    def update_time(self):
        # 这里我们假设 update_time 不需要任何参数
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)