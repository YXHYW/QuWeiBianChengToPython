"""
问题描述：抓交通肇事罪犯
一辆卡车肇事逃逸，有三个目击证人但都没记全车牌号，只有以下信息：
甲：牌照的前两位数字是相同的
乙：牌照的后两位数字是相同的，但与前两位不同
丙：四位的平方刚好是一个整数的平方
"""

def main():
    set1 = set(x**2 for x in range(31,100))
    for i in range(0,10):
        for j in range(0,10):
            if i != j:
                k = 1000*i + 100*i + 10*j +j
                if k in set1:
                    print("交通肇事犯的车牌号为：%s"%k)
                    break

if __name__ == "__main__":
    main()