from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, \
    QScrollArea, QWidget, QPushButton
from PyQt5.QtGui import QFont
import sqlite3

class NumberEdit(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("号码编辑")
        self.setFixedSize(1000, 600)  # 设置对话框的固定大小
        self.setMinimumSize(300, 200)  # 设置对话框的最小大小
        self.setMaximumSize(1000, 800)  # 设置对话框的最大大小

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # 设置滚动区域自适应大小
        # 创建内部窗口部件，放置 Label 和 LineEdit
        inner_widget = QWidget()
        layout = QVBoxLayout(inner_widget)
        self.label_list = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪', '红', '绿', '蓝', '红单', '绿单',
                      '蓝单', '红双', '绿双', '蓝双', '单', '双', '合单', '合双', '大', '小', '金', '木', '水', '火', '土', '尾大',
                      '尾小']
        self.line_edits = []  # 存储所有QLineEdit的引用
        # 添加 Label 和 LineEdit
        for label_name in self.label_list:
            label = QLabel(label_name)
            label.setFont(QFont("Arial", 10, QFont.Bold))  # 设置加粗字体
            label.setFixedSize(50, 40)  # 设置 Label 的固定大小
            line_edit = QLineEdit()
            line_edit.setStyleSheet("font-weight: bold; font-size: 12pt;")  # 设置LineEdit中文本的加粗显示
            line_edit.setFixedSize(800, 40)  # 设置 LineEdit 的固定大小
            line_edit.textChanged.connect(self.format_input)  # 连接文本变化信号到槽函数
            hbox_layout = QHBoxLayout()
            hbox_layout.addWidget(label)
            hbox_layout.addWidget(line_edit)
            layout.addLayout(hbox_layout)
            self.line_edits.append(line_edit)  # 将line_edit添加到列表中

        # 创建水平布局来放置按钮
        button_layout = QHBoxLayout()

        # 创建两个按钮
        button1 = QPushButton("清空")
        button2 = QPushButton("保存")

        # 将按钮添加到水平布局中
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        scroll_area.setWidget(inner_widget)

        # 在主垂直布局中添加滚动区域和按钮布局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)
        button1.clicked.connect(self.clear_line_edit)  # 清空所有输入
        button2.clicked.connect(self.save_to_database)  # 表格保存键
    def format_input(self, text):
        # 去除非数字字符
        text = ''.join(filter(str.isdigit, text))
        # 检查每两个数字组合是否在 01 到 49 范围内
        first_num_list = []
        second_num_list = []
        filtered_list = []
        temp_list = []
        # 判断第一个数字在0-4之间，第二个数字在0-9之间， 具体就是检查每两个数字组合是否在 01 到 49 范围内
        for index in range(len(text)):
            if index % 2 == 0 and 0 <= int(text[index]) <= 4:
                first_num_list.append((text[index]))
            elif index % 2 != 0 and 0 <= int(text[index]) <= 9:
                second_num_list.append(text[index])
        try:
            for i in range(len(first_num_list)):
                filtered_list.append(first_num_list[i])
                filtered_list.append(second_num_list[i])
        except:
            # 这里不处理是为了让lineEdit能正常显示
            pass
        # 通过flag来控制数字的组合，当索引 > 2时，根据flag来组合，i需要自增1，因为每组合一个数字，与filtered_list的索引差距就会增加1
        flag = False
        i = 1
        for x in range(len(filtered_list)):
            if x > 0 and (x + 1) % 2 == 0 and not flag:
                temp_list.append(filtered_list[x-1] + filtered_list[x])
            elif x > 0 and (x + 1) % 2 != 0 and not flag:
                temp_list.append(filtered_list[x])
                flag = True
                continue
            if flag:
                i += 1
                temp_list[x-i] = filtered_list[x-1] + filtered_list[x]  # 注意：这里filtered_list的索引不需要 - i
                flag = False

        if temp_list:
            result_string = ' '.join(temp_list)  # 当temp_list有值时，就正常录入
        else:
            result_string = ' '.join(filtered_list)  # 保证第一个数字输入时，能录入
        sender = self.sender()
        sender.setText(result_string)

    def clear_line_edit(self):
        # 清除所有QLineEdit的内容
        for line_edit in self.findChildren(QLineEdit):
            line_edit.clear()

    def save_to_database(self):
        # 连接到 SQLite 数据库
        connection = sqlite3.connect('../sql/number_edit.db')
        cursor = connection.cursor()

        # 创建表格，如果表格不存在
        cursor.execute('''CREATE TABLE IF NOT EXISTS number_edit (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          label TEXT UNIQUE,
                          value TEXT)''')
        # # 清空表格
        # cursor.execute('DELETE FROM number_edit')
        # cursor.execute('DELETE FROM sqlite_sequence WHERE name="number_edit"')  # 重置id计数
        # 获取所有 QLineEdit 的值，并插入数据库
        for label, line_edit in zip(self.label_list, self.line_edits):
            value = line_edit.text()
            if value:
                # 查询数据库中是否存在相同的 label
                cursor.execute('SELECT * FROM number_edit WHERE label = ?', (label,))
                existing_row = cursor.fetchone()
                if existing_row:
                    # 如果存在相同的 label，则更新该行的 value 值
                    cursor.execute('UPDATE number_edit SET value = ? WHERE label = ?', (value, label))
                else:
                    # 如果不存在相同的 label，则插入新的行
                    cursor.execute('INSERT INTO number_edit (label, value) VALUES (?, ?)', (label, value))

        # 提交事务并关闭连接
        connection.commit()

        # cursor.execute('SELECT * FROM number_edit')
        # results = cursor.fetchall()
        # print('-------', results)
        connection.close()

        # 提示保存成功
    def show_dialog(self):
        self.dialog = NumberEdit()
        self.dialog.exec_()



