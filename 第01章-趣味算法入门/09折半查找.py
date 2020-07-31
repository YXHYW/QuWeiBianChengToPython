"""
问题描述：
N 个有序整数数列已放在一维数组中，利用二分查找法查找整数m在数组中的位置。若找到，输出下标；反之，输出“Not be found!”
"""
from numpy.random import randint

def zheBanSearch(nums:list[int],target:int):
    k = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = nums[mid]
        if guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
        else:
            k = mid
            break
    if k >= 0:
        print("已找到{0}，其在列表中的index为：{1}".format(target,k))
    else:
        print("Not be found!") 



if __name__ == "__main__":
    nums = list(randint(0,10,size=19))
    nums_sorted = sorted(nums)
    target = 5
    print(nums)
    print(nums_sorted)
    zheBanSearch(nums_sorted,target)