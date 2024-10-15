# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        curr = 1
        while curr + 1 < len(flowerbed):
            # print(n, flowerbed, curr)
            if (
                flowerbed[curr - 1]
                == flowerbed[curr]
                == flowerbed[curr + 1]
                == 0
            ):
                flowerbed[curr] = 1
                n -= 1
                if n == 0:
                    return True
            curr += 1
        return False
