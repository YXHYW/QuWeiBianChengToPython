"""
问题描述：给定一个M进制的数x，实现对x向任意一个非M进制的数的转换。

Python内置了二进制、八进制、十进制、十六进制转换的函数
"""
def bin2dec(str_num:str):
    # 二进制转十进制
    # 参数为数字字符串
    return str(int(str_num,2))

def hex2dec(str_num:str):
    # 十六进制转十进制
    return str(int(str_num.upper(),16))

def oct2dec(str_num:str):
    # 八进制转十进制
    return str(int(str_num,8))

"""
十进制转二进制：bin()
十进制转八进制：oct()
十进制转十六进制：hex()
十六进制转二进制：bin(int(str,16))
二进制转十六进制：hex(int(str,2))
"""