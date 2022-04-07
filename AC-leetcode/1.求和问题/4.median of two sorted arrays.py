"""
两个排好序的array：nums1，nums2，长度分别为m，n，返回他们的中位数
The overall run time complexity should be O(log (m+n))
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
"""
如果两个list的长度为奇数，找到中间元素，否则计算中间对的平均值。
get_kth_smallest 函数递归移除 k//2 元素，每次递归调用移除比中位数小的一半元素
Time-O(log(m+n)), Space-O(log(m+n)), 递归调用stack
"""


def findMedianSortedArrays(A, B):
    def get_kth_smallest(a_start, b_start, k):
        # if k <= 0 or k > len(nums1) - a_start + len(nums2) - b_start:
        # base cases
        if a_start >= len(A):
            ta = b_start + k
            res = B(ta - 1)
            return B[res]

        if b_start >= len(B):
            tb = a_start + k
            res = A(tb - 1)
            return A[res]

        if k == 1:
            return min(A[a_start], B[b_start])

        # 移除 k//2 elements, 递归，从两个list中找到第 k//2 -1 个最小元素，第 k//2 -1 个元素必定存在于其中一个list
        mid_A, mid_B = float('inf'), float('inf')
        if k // 2 - 1 < len(A) - a_start:
            mid_A = A[a_start + k // 2 - 1]
        if k // 2 - 1 < len(B) - b_start:
            mid_B = B[b_start + k // 2 - 1]

        if mid_A < mid_B:
            return get_kth_smallest(a_start + k // 2, b_start, k - k // 2)

        return get_kth_smallest(a_start, b_start + k // 2, k - k // 2)

    right = get_kth_smallest(0, 0, 1 + (len(A) + len(B)) // 2)
    if len(A) + len(B) % 2 == 1:
        return right

    left = get_kth_smallest(0, 0, (len(A) + len(B)) // 2)

    return (left + right) / 2.0


nums1 = [1, 2]
nums2 = [3]
print(findMedianSortedArrays(A=nums1, B=nums2))
