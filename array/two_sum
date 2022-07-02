# https://leetcode.com/problems/two-sum/


# single pass

# 1. Create empty hashable aux space having search O(1) and add elements of the input array on the traversal.

# 2a. lets say num = [a,b,C1,d,e,f,C2,h,]  and C1 + C2 == target
# 2b. when you reach C2, C1 would already be there in aux space
# 2c.  and can be retrieved in O(1) by using eq: C1 = target - C2


def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n  # 2b
        if m in d:  # 2c
            return [d[m], i]
        else:
            d[n] = i  # point 1 above


twoSum([2, 7, 11, 15], 9)
