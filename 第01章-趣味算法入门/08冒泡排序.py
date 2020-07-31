"""
对 N 个整数进行升序排列
"""
from numpy.random import randint
from time import time

def maoPaoSort(nums:[int]):
    length = len(nums)
    for i in range(length-1):
        for j in range(length - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

if __name__ == "__main__":
    nums = list(randint(100,1000,size=100))
    print("原列表为：",nums)
    start = time()
    print("排序后为：",maoPaoSort(nums))
    end = time()
    print("用时：",end-start)