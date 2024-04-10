from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QKeyEvent, QInputMethodEvent, QFont, QTextCursor
from PyQt5.QtCore import Qt, QMimeData
import re
class TextEditRestrict(QTextEdit):
    def __init__(self, parent=None):
        super(TextEditRestrict, self).__init__(parent)
        self.setAttribute(Qt.WA_InputMethodEnabled, False)  # 禁用输入法
        # # 设置默认字体大小
        # self.setFontPointSize(12)
        # self.setFontWeight(QFont.Bold) #字体加粗
        # # 设置默认字体颜色
        # self.setTextColor(QColor(Qt.black))  # 使用黑色作为默认字体颜色

        # 你也可以设置默认字体，如果需要的话
        self.setFont(QFont("Arial", 12))
        self.num = 0
    def insertFromMimeData(self, source: QMimeData) -> None:
        # 阻止通过粘贴操作输入中文
        if source.hasText():
            text = source.text()
            if not self._contains_chinese(text):
                super().insertFromMimeData(source)

    def _contains_chinese(self, text: str) -> bool:
        # 检查字符串是否包含中文
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                return True
        return False

    def inputMethodEvent(self, event: QInputMethodEvent) -> None:
        # 阻止通过输入法输入中文
        pass  # 不调用父类的 inputMethodEvent 方法

    def count_digits_in_string(self,s):
        # 使用正则表达式匹配字符串中的数字
        digits = re.findall(r'\d', s)
        # 返回数字的个数
        return len(digits)
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if self.toPlainText() and self.num % 2 == 0 and event.key() not in [Qt.Key_Backspace, Qt.Key_Delete] and \
                self.toPlainText()[-1] != ' ' and '=' not in self.toPlainText():
            self.insertPlainText(' ')
        # 检查按键是否是数字、删除键、回退键或方向键等
        if event.key() in [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
                            Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]:

            super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
            self.num = self.count_digits_in_string(self.toPlainText())

        elif event.key() in [Qt.Key_Backspace, Qt.Key_Delete]:

            # 处理删除键
            super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
            self.num = self.count_digits_in_string(self.toPlainText())
            self.char_counter = max(0, self.char_counter - 1)  # 减少char_counter的计数，但确保它不会变成负数


        if (event.key() in [ Qt.Key_Left, Qt.Key_Right,
                                Qt.Key_Up, Qt.Key_Down, Qt.Key_Home, Qt.Key_End, Qt.Key_PageUp,
                                Qt.Key_PageDown, Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt, Qt.Key_Return, Qt.Key_Enter] or \
                event.key() == Qt.Key_Period):
            if event.key() == Qt.Key_Period:
                self.insertPlainText(' = ')  # 当按下.键时插入=
            else:
                super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
        else:
            event.ignore()

