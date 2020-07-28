"""
问题描述：兔子产子的斐波拉契问题
30个月内，每个月有多少对兔子
"""
def main():
    a=b=1
    for i in range(1,31):
        if i <= 2:
            print("在第{0}月，有兔子1对".format(i))
        else:
            c = a + b
            print("在第{0}月，有兔子{1}对".format(i,c))
            b = a
            a = c

if __name__ == "__main__":
    main()