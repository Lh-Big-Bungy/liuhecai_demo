class Normal_button_click():
    def copy_text_to_browser(self):
        # 从第一个 QTextEdit 读取内容
        text = self.restricted_textedit.toPlainText()
        # 将内容设置到第二个 QTextEdit
        self.textBrowser.setText(text)