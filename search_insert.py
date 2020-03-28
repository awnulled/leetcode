from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
    

obj = Solution()
arr = [1,3,5,6]
trg = 7
print(obj.searchInsert(arr, trg))