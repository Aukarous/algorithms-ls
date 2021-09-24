"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""
# def reverse(x: int) -> int:
#     negative = x < 0
#     x = abs(x)
#     reversed = 0
#     while x !=0:
#         reversed = reversed * 10 + x % 10     # % 取余
#         x //= 10

#     if reversed > 2 **31 -1:
#         return 0
#     return reversed if not negative else -reversed


# x = -123
# print(reverse(x))

def reversed(x):
    negative = x < 0
    x = abs(x)
    a = list(str(x))
    a.reverse()
    res = 0
    for i in range(len(a),0,-1):
        res += int(a[len(a)-i]) * 10**(len(a)-1)

    return a if negative else -a

x = -124
print(reversed(x))