from PyQt5.QtWidgets import QDialog, QMessageBox
import re
class SeqInput(QDialog):

    def __init__(self, seq_input, restricted_textedit):
        super().__init__()
        self.seq_input = seq_input
        self.restricted_textedit = restricted_textedit
    def data_processing(self):
        text = self.seq_input.text()
        print(text)
        # 定义正则表达式，匹配除了数字、等号和减号之外的字符
        pattern = re.compile(r'[^0-9\-=]')
        # 使用正则表达式进行匹配
        match = pattern.search(text)
        # 如果找到了匹配项，表示字符串包含了除了数字、等号和减号之外的字符
        if match or not text:
            QMessageBox.warning(self, "错误", "只允许输入数字、负号和等号")
            self.seq_input.clear()  # 清空当前错误输入
        else:
            try:
                money = text.split('=')[1]    ## 分离出投注数额
                text = text[:text.index("=")]
                text_list = text.split('-')
                if int(text_list[1]) < int(text_list[0]):
                    QMessageBox.warning(self, "错误", "第二个数字比第一个小，请重新输入")
                    self.seq_input.clear()  # 清空当前错误输入
                    return  # 结束执行
                if 1 <= int(text_list[0]) <= 49 and 1 <= int(text_list[1]) <= 49:
                    self.copy_text_to_textedit(text_list[0], text_list[1], money)
                    QMessageBox.information(self, "正确", "输入正确")
                    return  # 结束执行
                else:
                    QMessageBox.warning(self, "错误", "号码输入不正确，请规范输入数字")
                    self.seq_input.clear()  # 清空当前错误输入
                    return  # 结束执行
            except:
                QMessageBox.warning(self, "错误", "此处为连号输入，请按照右侧提示，规范输入数字")
                self.seq_input.clear()  # 清空当前错误输入
                return  # 结束执行
    def copy_text_to_textedit(self, first_num, second_num, money):
        num_str = ''
        for i in range(int(first_num), int(second_num)+1):
            if i < 10:
                i = '0' + str(i)
                num_str += str(i)
            else:
                num_str += str(i)
            num_str += ' '

        num_str = num_str + ' ' + '=' + ' ' + money
        self.restricted_textedit.append(num_str)