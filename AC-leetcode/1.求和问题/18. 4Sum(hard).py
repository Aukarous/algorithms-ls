"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
递归，化解为2sum问题
"""
from typing import List


class Solution:
    ELEMENTS = 4
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, res)
        return res
    
    def n_sum(self, nums, target, partial, n, results):
        if len(nums) < n or target > nums[-1] * n or target < nums[0] * n:
            # early return if possible
            return
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while nums[right] == nums[right + 1] and right > left:
                        # 如果target找到，移动到下一个不同的number
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        else:
            for i in range(len(nums) - n + 1):
                # for all possible first numbers nums[i]
                if i == 0 or nums[i] != nums[i - 1]:
                    # if not duplicate:
                    self.n_sum(nums[i + 1:], target - nums[i], partial + [nums[i]], n - 1, results)


s = Solution()
print(s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
