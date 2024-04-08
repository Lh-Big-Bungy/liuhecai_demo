import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QKeyEvent, QInputMethodEvent
from PyQt5.QtCore import Qt, QMimeData

class ChineseRestrictedTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(ChineseRestrictedTextEdit, self).__init__(parent)
        self.setAttribute(Qt.WA_InputMethodEnabled, False)  # 禁用输入法

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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 检查按键是否是数字、删除键、回退键或方向键等
        if (event.key() in [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
                            Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9] or
                event.key() in [Qt.Key_Backspace, Qt.Key_Delete, Qt.Key_Left, Qt.Key_Right,
                                Qt.Key_Up, Qt.Key_Down, Qt.Key_Home, Qt.Key_End, Qt.Key_PageUp,
                                Qt.Key_PageDown, Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt, Qt.Key_Return, Qt.Key_Enter]):
            super(ChineseRestrictedTextEdit, self).keyPressEvent(event)  # 调用父类的keyPressEvent处理
        else:
            event.ignore()



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.textEdit = ChineseRestrictedTextEdit()
        layout.addWidget(self.textEdit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Integer TextEdit')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())