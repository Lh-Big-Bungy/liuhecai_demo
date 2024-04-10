import re


def count_digits_in_string(s):
    # 使用正则表达式匹配字符串中的数字  
    digits = re.findall(r'\d', s)
    # 返回数字的个数  
    return len(digits)
s='12'
a=count_digits_in_string(s)
print(a)