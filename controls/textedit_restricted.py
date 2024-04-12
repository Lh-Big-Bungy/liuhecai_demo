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
        self.restrict_flag = True
        self.current_line_text = ''
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
        self.current_line_text = self.textCursor().block().text()  # 当前行内容每次都需更新
        # 限制不能输入 号码00
        if event.key() == Qt.Key_0 and self.current_line_text and self.num % 2 == 1 and self.restrict_flag \
                and self.current_line_text[-1] == '0':
            event.ignore()
            return
        # 每输入两个数字，自动添加空格
        if self.current_line_text and self.num % 2 == 0 and event.key() not in [Qt.Key_Backspace, Qt.Key_Delete] and \
                self.current_line_text[-1] != ' ' and self.restrict_flag:
            self.insertPlainText(' ')
        # 按下回车键后重置为 每输入两个数字，自动添加空格
        elif event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.restrict_flag = True
            self.current_line_text = ''
            super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
        # 计算当前行的数字个数
        if event.key() in [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_Backspace, Qt.Key_Delete]:
            super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
            self.current_line_text = self.textCursor().block().text()  # 当前行内容每次都需更新
            print(self.current_line_text)
            self.num = self.count_digits_in_string(self.current_line_text)
            if '=' not in self.current_line_text:
                self.restrict_flag = True
            else:
                self.restrict_flag = False

        if event.key() in [Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]:
            # 限制输入数字大小 1-49
            if ((self.current_line_text and self.num % 2 == 0) or self.num == 0) and self.restrict_flag:
                try:
                    self.current_line_text = self.textCursor().block().text()  # 当前行内容每次都需更新
                    digit = int(self.current_line_text[-1])
                    if digit > 4:
                        event.ignore()
                except:
                    event.ignore()

            else:
                super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
                self.current_line_text = self.textCursor().block().text()  # 当前行内容每次都需更新
                self.num = self.count_digits_in_string(self.current_line_text)
        elif event.key() in [ Qt.Key_Left, Qt.Key_Right,
                                Qt.Key_Up, Qt.Key_Down, Qt.Key_Home, Qt.Key_End, Qt.Key_PageUp,
                                Qt.Key_PageDown, Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt, Qt.Key_Period]:
            if event.key() == Qt.Key_Period:
                self.restrict_flag = False
                if self.num % 2 == 0:
                    self.insertPlainText('= ')  # 当按下.键时插入=
                else:
                    self.insertPlainText(' = ')  # 当按下.键时插入=
            else:
                super(TextEditRestrict, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理

        else:
            event.ignore()

