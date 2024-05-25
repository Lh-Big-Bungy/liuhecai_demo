import sqlite3
class DataToSql():
    def __init__(self, data='', odds='', loss=''):
        self.data = data
        self.odds = odds
        self.loss = loss

    def data_to_dict(self):
        num_dict = {}
        text_list = self.data.split('\n')
        for text in text_list:
            temp_list = text.split('=')
            num_list = temp_list[0].split(' ')
            num_list = [item for item in num_list if item != ""]  # 清除空元素
            money = temp_list[1].split(' ')
            money = [item for item in money if item != ""]  # 清除空元素
            for num in num_list:
                if not (1 <= int(num) <= 49):
                    continue
                key = num
                key = str(key).zfill(2)  # 自动补全为两位数字，小于10时，自动在前面加0，例01、09
                value = int(money[0])
                if key in num_dict:
                    num_dict[key] += value
                else:
                    num_dict[key] = value
        return num_dict
    def write_to_database(self):
        self.num_dict = self.data_to_dict()
        try:
            # 连接到数据库
            connection = sqlite3.connect('../sql/official_data.db')
            cursor = connection.cursor()


            # 创建表（如果表不存在）
            cursor.execute('''CREATE TABLE IF NOT EXISTS official_data_table
                                (id INTEGER PRIMARY KEY, num TEXT, money INTEGER)''')
            # 每次执行前清空数据库
            cursor.execute("DELETE FROM official_data_table")
            # 插入数据

            for key, value in self.num_dict.items():
                cursor.execute("INSERT INTO official_data_table (num, money) VALUES (?, ?)", (key, value))

            # 提交更改并关闭连接
            connection.commit()
            connection.close()

        except Exception as e:
            print("写入数据库时出错:", e)

    def odds_loss_to_database(self):
        try:
            # 连接到数据库
            connection = sqlite3.connect('../sql/official_data.db')
            cursor = connection.cursor()
            # 创建表（如果表不存在）
            cursor.execute('''CREATE TABLE IF NOT EXISTS odds_loss_table
                                       (id INTEGER PRIMARY KEY, odds TEXT, loss INTEGER)''')
            # 每次执行前清空数据库
            cursor.execute("DELETE FROM odds_loss_table")

            # 插入数据
            cursor.execute("INSERT INTO odds_loss_table (odds, loss) VALUES (?, ?)", (self.odds, self.loss))
            # 提交更改并关闭连接
            connection.commit()

            connection.close()

        except Exception as e:
            print("写入数据库时出错:", e)