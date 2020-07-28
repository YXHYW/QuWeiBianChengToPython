"""
问题描述：打鱼还是晒网
某人从1990年1月1日起开始“三天打鱼两天晒网”，问这个人在以后的某一天中是打鱼还是晒网？
"""
from datetime import datetime
def main():
    source_date = datetime(1990,1,1)
    target_date = datetime.now()
    Cha = (target_date - source_date).days
    if Cha % 5 <= 3:
        print("今天打鱼！")
    else:
        print("今天晒网")

if __name__ == "__main__":
    main()