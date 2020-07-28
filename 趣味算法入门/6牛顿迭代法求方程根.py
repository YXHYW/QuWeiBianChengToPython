"""
问题描述：
编写用牛顿迭代法求方程根的函数。方程为ax^3 + bx^2 + cx + d = 0，系数a,b,c,d由主函数输入。求x在1附近的一个实根。求出根后，由主函数输出。
"""
from math import pow

def solution(a,b,c,d):
    x = 1.5
    while True:
        x0 = x
        f = a*x0**3 + b*x0**2 + c*x0 + d
        fd = 3*a*x0*x0 + 2*b*x0 + c
        h = f/fd
        x = x0-h
        if abs(x-x0) >= pow(10,-5):
            break
    return x

if __name__ == "__main__":
    # a = int(input("请输入系数a："))
    # b = int(input("请输入系数b："))
    # c = int(input("请输入系数c："))
    # d = int(input("请输入系数d："))
    print(solution(2,-4,3,-6))
    # print(type(solution(a,b,c,d)))

"""
可以直接用sympy直接求解一元三次方程
import sympy as sp
x = sp.Symbol('x')
f = 2*x**3 - 4*x**2 + 3*x -6
x = sp.solve(f)
print(x)
"""