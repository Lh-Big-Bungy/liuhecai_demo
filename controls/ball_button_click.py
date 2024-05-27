from PyQt5.QtWidgets import QMessageBox
import re
import sqlite3
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
                if not i:
                    continue
                if '=' not in i or i.strip().split(' ')[-1] == '=':
                    QMessageBox.warning(self.restricted_textedit, "错误", "未输入等号与金额，示例：10 20 30 = 10")
                    return
                elif i.count('=') != 1:
                    QMessageBox.warning(self.restricted_textedit, "错误", "请勿输入多个等号")
                    return
                temp_list = i.split('=')
                num_list = temp_list[0].split(' ')
                num_list = [item for item in num_list if item != ""]  # 清除空元素
                for num in num_list:
                    if not (1 <= int(num) <= 49):
                        QMessageBox.warning(self.restricted_textedit, "错误", "请输入01-49之间的正确号码")
                        return
                money = temp_list[1].split(' ')
                money = [item for item in money if item != ""]  # 清除空元素
                if int(money[0]) == 0:
                    QMessageBox.warning(self.restricted_textedit, "错误", "有号码投注金额为零，请重新确认")
                    return

        # 将内容设置到第二个 QTextEdit
        self.textBrowser.setText(text)

    def get_number_from_number_edit(self, label):
        try:
            # 连接到 SQLite 数据库
            connection = sqlite3.connect('sql/number_edit.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM number_edit WHERE label = ?', (label,))
            results = cursor.fetchone()
            connection.close()
            # 返回查询结果
            if results and results[2]:
                return results[2]  # 返回 value 值
            else:
                return None  # 如果没有找到对应的 label，返回 None
        except Exception as e:
            print(e)

    def on_color_button_clicked(self, label):
        number_list = self.get_number_from_number_edit(label)
        if number_list:
            # 在 QTextEdit 中添加数字
            self.restricted_textedit.append(number_list)
        else:
            label = "<b><font color='red'>{}</font></b>".format(label)
            QMessageBox.warning(self.restricted_textedit, "错误",
                                "未设置{}的号码，请点击“号码编辑”，找到{}并且重新设置".format(label, label))

    def red_on_button_clicked(self):
        self.on_color_button_clicked('红')

    def green_on_button_clicked(self):
        self.on_color_button_clicked('绿')

    def blue_on_button_clicked(self):
        self.on_color_button_clicked('蓝')

    def mouse_on_button_clicked(self):
        self.on_color_button_clicked('鼠')

    def bull_on_button_clicked(self):
        self.on_color_button_clicked('牛')

    def tiger_on_button_clicked(self):
        self.on_color_button_clicked('虎')

    def rabbit_on_button_clicked(self):
        self.on_color_button_clicked('兔')

    def dragon_on_button_clicked(self):
        self.on_color_button_clicked('龙')

    def snake_on_button_clicked(self):
        self.on_color_button_clicked('蛇')

    def horse_on_button_clicked(self):
        self.on_color_button_clicked('马')

    def goat_on_button_clicked(self):
        self.on_color_button_clicked('羊')

    def monkey_on_button_clicked(self):
        self.on_color_button_clicked('猴')

    def chicken_on_button_clicked(self):
        self.on_color_button_clicked('鸡')

    def dog_on_button_clicked(self):
        self.on_color_button_clicked('狗')

    def pig_on_button_clicked(self):
        self.on_color_button_clicked('猪')

    def red_single_on_button_clicked(self):
        self.on_color_button_clicked('红单')

    def red_even_on_button_clicked(self):
        self.on_color_button_clicked('红双')

    def green_single_on_button_clicked(self):
        self.on_color_button_clicked('绿单')

    def green_even_on_button_clicked(self):
        self.on_color_button_clicked('绿双')

    def blue_single_on_button_clicked(self):
        self.on_color_button_clicked('蓝单')

    def blue_even_on_button_clicked(self):
        self.on_color_button_clicked('蓝双')

    def single_on_button_clicked(self):
        self.on_color_button_clicked('单')

    def composite_single_on_button_clicked(self):
        self.on_color_button_clicked('合单')

    def even_on_button_clicked(self):
        self.on_color_button_clicked('双')

    def composite_even_on_button_clicked(self):
        self.on_color_button_clicked('合双')

    def large_on_button_clicked(self):
        self.on_color_button_clicked('大')

    def minor_on_button_clicked(self):
        self.on_color_button_clicked('小')

    def gold_on_button_clicked(self):
        self.on_color_button_clicked('金')

    def wood_on_button_clicked(self):
        self.on_color_button_clicked('木')

    def water_on_button_clicked(self):
        self.on_color_button_clicked('水')

    def fire_on_button_clicked(self):
        self.on_color_button_clicked('火')

    def soil_on_button_clicked(self):
        self.on_color_button_clicked('土')

    def tail_large_on_button_clicked(self):
        self.on_color_button_clicked('尾大')

    def tail_minor_on_button_clicked(self):
        self.on_color_button_clicked('尾小')

