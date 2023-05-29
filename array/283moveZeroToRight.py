from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0 
    while nums[left] != 0:
        left =+ 1
    right = left + 1
    while right < len(nums):
        if nums[right] == 0 :
            right += 1
            continue
        
        # right is at first non -zero number after left
        nums[left] = nums[right]



