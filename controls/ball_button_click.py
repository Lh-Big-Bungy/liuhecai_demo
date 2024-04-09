class ButtonClick():
    def __init__(self, restricted_textedit, textBrowser):
        self.restricted_textedit = restricted_textedit
        self.textBrowser = textBrowser
    def copy_text_to_browser(self):
        # 从第一个 QTextEdit 读取内容
        text = self.restricted_textedit.toPlainText()
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