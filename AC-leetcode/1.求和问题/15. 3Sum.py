"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

排序，对每个i，在其他更高的值执行双向搜索。跳过重复值，
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                print(i, j, k)
                triple_sum = nums[i] + nums[j] + nums[k]
                if triple_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
                elif triple_sum > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return res


s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
