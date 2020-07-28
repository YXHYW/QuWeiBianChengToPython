"""
问题描述：
百钱百鸡问题：一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱。现在要用百钱买百鸡，请问公鸡、母鸡、小鸡各有多少只？
"""

def main():
    for x in range(0,21):
        for y in range(0,34):
            z = 100 - x - y
            if z % 3 == 0 and x + y + z == 100 and 5*x + 3*y + z/3 == 100:
                print("公鸡有{0}，母鸡有{1}，小鸡有{2}".format(x,y,z))

if __name__ == "__main__":
    main()