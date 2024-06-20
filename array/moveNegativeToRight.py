# # # 1.	place all negative element at the end of array without changing the order of positive element and negative element.

# # # Input:
# # # N=8
# # # arr [] = {-5, 7, -3, -4, 9, 10, -1, 11}
# # # Output:
# # # 7 9 10 11 -5 -3 -4 -1

# # # Input:
# # # N = 8
# # # arr [] = {1, -1, 3, 2, -7, -5, 11, 6}
# # # Output:
# # # 1 3 2 11 6 -1 -7 -5


def way1(nums):
    positive = []
    negative = []
    for num in nums:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    positive.extend(negative)
    return positive


nums = [-5, 7, -3, -4, 9, 10, -1, 11]

# way1(nums)


nums = [-5, 7, -3, -4, 9, 10, -1, 11]


def way2(nums):
    nums.insert(0, float("inf"))
    nums.append(float("-inf"))

    loc_positive = 0
    next_positive = loc_positive + 1
    while loc_positive < len(nums):
        while nums[next_positive] < 0 and next_positive < len(nums):
            next_positive += 1
        nums[loc_positive], nums[next_positive] = (
            nums[next_positive],
            nums[loc_positive],
        )
        loc_positive = next_positive
        next_positive = loc_positive + 1

    return nums


way2(nums)
