"""
问题描述：
小明有5本新书，要借给A、B、C这三位小朋友，若每人每次只能借一本，则可以有多少种不同的借法？
"""

def main():
    a=b=c=i=0
    print("A, B, C 三人所选的书号分别为：")
    for a in range(1,6):
        for b in range(1,6):
            for c in range(1,6):
                if a!=b and a!=c and c!=b:
                    print("A:{0}, B:{1}, C{2}".format(a,b,c))
                    i += 1
                    if i%4 ==0:
                        print("\n")
    print("共有{0}种有效借阅的方法".format(i))

if __name__ == "__main__":
    main()