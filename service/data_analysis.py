import sqlite3
import random
import os
def random_seed(key_list):
    # 生成真随机种子
    true_random_seed = os.urandom(32)  # 32字节的真随机种子

    # 使用真随机种子设置伪随机数生成器的种子
    random.seed(true_random_seed)
    # 从列表中随机选择一个元素
    random_choice = random.choice(key_list)
    return random_choice
class DataAnalysis():
    def get_data_from_sql(self):
        # 连接到数据库
        connection = sqlite3.connect('sql/official_data.db')
        cursor = connection.cursor()
        # 执行倍率、预亏损查询
        cursor.execute("SELECT * FROM odds_loss_table")

        # 获取倍率、预亏损查询结果
        self.odds_loss = cursor.fetchall()
        #print(self.odds_loss)

        # 执行号码、投注金额查询
        cursor.execute("SELECT * FROM official_data_table")

        # 获取号码、投注金额查询结果
        self.num_money = cursor.fetchall()

        #print(self.num_money)
        # 关闭游标和连接
        cursor.close()
        connection.close()
    def bet_again(self, times):
        temp_list = self.key_list[:]  # 浅复制，通过切片；直接浅复制会同时改变self.key_list的值
        for i in range(times):
            num = random_seed(temp_list)
            temp_list.remove(num)  # 每次随机挑选都把挑过的从待挑选列表删除，直到全部随机完，再重置待挑选列表
            self.catch_dict[num] += 1
            self.pop_dict[num] -= 1
            if not temp_list:
                temp_list = self.key_list[:]
    def data_analysis(self):
        self.num_money_dict = {}
        self.get_data_from_sql()
        self.odds = int(self.odds_loss[0][1])
        self.base_loss = int(self.odds_loss[0][2])
        for i in self.num_money:
            self.num_money_dict[i[1]] = i[2]
        self.pop_dict = {}  # 应抛出字典
        self.catch_dict = {}  # 应吃进字典
        self.win_money = 0  # 吃进所赚的钱
        self.key_list = []  # 超预亏损号码列表
        catch_money = 0  # 应吃进金额
        for key in self.num_money_dict.keys():
            if self.num_money_dict[key] * self.odds <= self.base_loss:  # 单个号码总注数*赔率仍达不到预亏值的，全部吃进
                self.catch_dict[key] = self.num_money_dict[key]  # 全吃进
                self.pop_dict[key] = 0  # 应抛出金额 = 单个号码总注数 - 吃进注数, 全吃进时为0
                self.win_money += self.num_money_dict[key]  # 吃进总金额增加
            elif self.num_money_dict[key] * self.odds > self.base_loss:
                catch_money = self.base_loss // self.odds  # 应吃进金额，向下取整
                self.win_money += catch_money  # 吃进总金额增加
                self.key_list.append(key)
                # 当预亏损金额过小，总金额增加但吃进金额不增加时，走这里，才能正常显示
                self.pop_dict[key] = self.num_money_dict[key] - catch_money  # 应抛出金额 = 单个号码总注数 - 吃进注数
                self.catch_dict[key] = catch_money  # 吃进 应吃进的最大注数
        temp_loss = self.base_loss + self.win_money  # 应吃进金额增加，所以预亏损值会增加，实际亏损值为最初设置的值，不变
        catch_money_temp = temp_loss // self.odds  # 应吃进金额，向下取整，因吃进金额增加，所以这个也会改变
        flag = True
        not_enough_list = []  # 吃进后，总金额增加后，又可以全吃进的号码列表
        while flag:
            if catch_money and self.key_list and catch_money_temp != catch_money:  # 当catch_money_temp和catch_money不一致时才继续循环
                for key in self.key_list:  # 上面是针对全部数字，这是针对经过第一轮筛选的数字
                    if self.num_money_dict[key] <= catch_money_temp and key not in not_enough_list:
                        self.catch_dict[key] = self.num_money_dict[key]  # 全吃进
                        self.pop_dict[key] = 0  # 应抛出金额 = 单个号码总注数 - 吃进注数, 全吃进时为0
                        self.win_money += (self.num_money_dict[key] - catch_money)
                        not_enough_list.append(key)
                    elif key not in not_enough_list:
                        self.pop_dict[key] = self.num_money_dict[key] - catch_money_temp  # 应抛出金额 = 单个号码总注数 - 吃进注数
                        self.catch_dict[key] = catch_money_temp  # 吃进 应吃进的最大注数
                        self.win_money += (catch_money_temp - catch_money)
                temp_loss = self.base_loss + self.win_money
                catch_money = catch_money_temp  # 判断吃进金额是否已达到最大值，若catch_money_temp == catch_money，则表明已吃到最大值
                catch_money_temp = temp_loss // self.odds  # 应吃进金额，向下取整
            else:

                flag = False
        if self.num_money_dict:  # 数据不为空时，才进行下列操作
            max_value_in_dict = max(self.num_money_dict.values())  # 当投注金额小于最大能吃进金额时，最大投注数应设为现有的最大数,最大亏损也应为现有最大数 * 倍率
            if catch_money_temp > int(max_value_in_dict):
                self.max_num = max_value_in_dict
                self.actual_loss_amount = max_value_in_dict * self.odds - self.win_money
            else:
                self.max_num = catch_money_temp
                self.actual_loss_amount = catch_money_temp * self.odds - self.win_money
            self.max_num_list = []
            for i in self.catch_dict.keys():
                if self.catch_dict[i] == self.max_num:
                    self.max_num_list.append(i)
        self.single_loss_max = catch_money_temp * self.odds   # 单个号码最大亏损值
        # for key in self.key_list:
        #     if self.num_money_dict[key] <= catch_money_temp:
        #         self.catch_dict[key] = self.num_money_dict[key]  # 全吃进
        #     else:
        #         self.pop_dict[key] = self.num_money_dict[key] - catch_money_temp  # 应抛出金额 = 单个号码总注数 - 吃进注数
        #         self.catch_dict[key] = catch_money_temp  # 吃进 应吃进的最大注数

        # if self.win_money > odds and self.key_list:  # 吃进金额大于倍数，可继续下注
        #     times = self.win_money // odds  # 计算完所吃进的金额后，可以多吃进的注数
        #     self.bet_again(times)  # 吃进金额大于倍数，可继续下注
        #     self.win_money += times
        #     while times >= odds:  # 若此时仍大于倍数，继续吃进，继续下注
        #         times = times // odds
        #         self.bet_again(times)
        #         self.win_money += times

    def data_to_sql(self):
        try:
            # 连接到数据库
            connection = sqlite3.connect('sql/official_data.db')
            cursor = connection.cursor()
            # 创建表（如果表不存在）
            cursor.execute('''CREATE TABLE IF NOT EXISTS catch_and_throw_table
                                       (id INTEGER PRIMARY KEY, num TEXT, total INTEGER, throw INTEGER, catch INTEGER)''')
            # 每次执行前清空数据库
            cursor.execute("DELETE FROM catch_and_throw_table")
            for key in self.num_money_dict.keys():
                # 检查字典中是否存在对应的键
                if key in self.pop_dict and key in self.catch_dict:
                    # 插入数据
                    cursor.execute("INSERT INTO catch_and_throw_table (num, total, throw, catch) VALUES (?, ?, ?, ?)",
                                   (key, self.num_money_dict[key], self.pop_dict[key], self.catch_dict[key]))
                elif key not in self.pop_dict and key in self.catch_dict:
                    # 插入数据
                    cursor.execute("INSERT INTO catch_and_throw_table (num, total, throw, catch) VALUES (?, ?, ?, ?)",
                                   (key, self.num_money_dict[key], 0, self.catch_dict[key]))
            # 提交更改并关闭连接
            connection.commit()

            connection.close()

        except Exception as e:
            print("写入数据库时出错:", e)

    def run(self):
        self.data_analysis()
        self.data_to_sql()
if __name__ == '__main__':
    DataAnalysis().run()

