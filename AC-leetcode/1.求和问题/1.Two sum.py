"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
前提：每个输入当且仅当只有一个答案，每个元素只能使用一次，返回数字可无序
"""
def twosum(nums,target):
    num_to_index = {}   # key is number, value is index in nums
    for i,num in enumerate(nums):
        if target - num in num_to_index:      # in num_to_index.keys()
            print("i = {}, num = {}".format(i,num))
            return [num_to_index[target - num], i]
         
        num_to_index[num] = i
    return []




nums = [3,2,4]
target = 6

print(twosum(nums,target))


