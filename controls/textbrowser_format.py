from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtGui import QFont
class TextBrowserFormat(QTextBrowser):
    def __init__(self, textBrowser, parent=None):
        super(TextBrowserFormat, self).__init__(parent)
        self.textBrowser = textBrowser
        # 设置默认字体样式和颜色
        self.set_text_browser_font_size(12)
    def set_text_browser_font_size(self, size):
        """
        设置 QTextBrowser 的字符大小。
        """
        font = QFont()
        font.setPointSize(size)
        font.setWeight(QFont.Bold)
        self.textBrowser.setFont(font)
