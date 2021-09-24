"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
"""  
import numpy as np
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        flag = False
        start = 0
        len1,len2,len3 = 1,1,1
        while (start+len1+len2+len3) <= len(num):
            num1 = int(num[start:start+len1])
            num2 = int(num[start+len1:start+len1+len2])
            num3 = int(num[start+len1+len2:start+len1+len2+len3])
            print(num1,num2,num3)
            if num1+num2>num3:
                len3+=1
                continue
             if num1+num2<num3:
                len2+=1
                len3+=1
                continue
            else:
                flag = True
                print('————————————————')
                print(num1,num2,num3)
                print('————————————————')
            # start+=1
            len1,len2,len3=(2,2,2)
        return flag

str_ = "199100199"
s = Solution()
print(s.isAdditiveNumber(str_))

# '1991100'