from PyQt5.QtWidgets import QMessageBox
import re
class ButtonClick():
    def __init__(self, restricted_textedit, textBrowser):
        self.restricted_textedit = restricted_textedit
        self.textBrowser = textBrowser

    def is_valid_string(self, text):
        # 正则表达式匹配只包含数字、空格和等于号的字符串
        pattern = r'^[0-9\s=]+$'
        # 使用 re.match 进行匹配，如果匹配成功返回匹配对象，否则返回 None
        match = re.match(pattern, text)
        # 如果匹配对象存在，则返回 True，否则返回 False
        return bool(match)
    def clear_textbrowser_input(self):
        self.textBrowser.clear()
    def copy_text_to_browser(self):
        # 从第一个 QTextEdit 读取内容
        text = self.restricted_textedit.toPlainText()
        if not text:
            QMessageBox.warning(self.restricted_textedit, "错误", "输入为空，请输入数据再提交")
            return
        elif not self.is_valid_string(text):
            QMessageBox.warning(self.restricted_textedit, "错误", "输入不规范，只允许输入数字、空格、等于号")
            return
        else:
            texts = text.split('\n')
            for i in texts:
                if '=' not in i or i.strip().split(' ')[-1] == '=':
                    QMessageBox.warning(self.restricted_textedit, "错误", "未输入等号与金额，示例：10 20 30 = 10")
                    return
        # 将内容设置到第二个 QTextEdit
        self.textBrowser.setText(text)
    def red_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('1 2 3')
    def green_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('4 5 6')
    def blue_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('7 8 9')