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
        connection = sqlite3.connect('../sql/official_data.db')
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
        num_money_dict = {}
        self.get_data_from_sql()
        odds = int(self.odds_loss[0][1])
        base_loss = int(self.odds_loss[0][2])
        for i in self.num_money:
            num_money_dict[i[1]] = i[2]
        print(num_money_dict)
        print(odds, base_loss)
        self.pop_dict = {}  # 应抛出字典
        self.catch_dict = {}  # 应吃进字典
        self.win_money = 0  # 吃进所赚的钱
        self.key_list = []  # 超预亏损号码列表
        for key in num_money_dict.keys():
            if num_money_dict[key] * odds <= base_loss:  # 单个号码总注数*赔率仍达不到预亏值的，全部吃进
                self.catch_dict[key] = num_money_dict[key]  # 全吃进
                self.win_money += num_money_dict[key]  # 吃进总金额增加
            elif num_money_dict[key] * odds > base_loss:
                catch_money = base_loss // odds  # 应吃进金额，向下取整
                self.win_money += catch_money  # 吃进总金额增加
                self.key_list.append(key)
                self.pop_dict[key] = num_money_dict[key] - catch_money  # 应抛出金额 = 单个号码总注数 - 吃进注数
                self.catch_dict[key] = catch_money  # 吃进 应吃进的最大注数
        if self.win_money > odds and self.key_list:  # 吃进金额大于倍数，可继续下注
            times = self.win_money // odds  # 计算完所吃进的金额后，可以多吃进的注数
            self.bet_again(times)  # 吃进金额大于倍数，可继续下注
            self.win_money += times
            while times >= odds:  # 若此时仍大于倍数，继续吃进，继续下注
                times = times // odds
                self.bet_again(times)
                self.win_money += times
        print(self.key_list)
        print(self.catch_dict)
        print(self.pop_dict)
        print(self.win_money)



if __name__ == '__main__':
    a = DataAnalysis()
    a.data_analysis()

