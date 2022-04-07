"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        l = len(nums)
        while i < l - 1:
            while j <= l - 1 and nums[i] == nums[j]:
                nums.pop(j)
                l = len(nums)
            
            i += 1
            j += 1
        return len(nums)
    
    def remove_2(self, nums):
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        
        return len(nums) - cnt


s = Solution()
print(s.remove_2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
