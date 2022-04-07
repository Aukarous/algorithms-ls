"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closets = float('inf')
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triple = nums[i] + nums[j] + nums[k]
                if triple == target:
                    return target
                
                if abs(triple - target) < abs(closets - target):
                    closets = triple
				
                if triple - target > 0:
                    k -= 1
                else:
                    j += 1
        
        return closets


s = Solution()
print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
