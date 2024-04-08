class Button_click():
    def __init__(self, restricted_textedit):
        self.restricted_textedit = restricted_textedit
    def red_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('1 2 3')
    def green_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('4 5 6')
    def blue_on_button_clicked(self):
        # 在 QTextEdit 中添加数字
        self.restricted_textedit.append('7 8 9')