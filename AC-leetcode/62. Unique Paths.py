"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 
Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""
def uniquePaths( m: int, n: int):
    if m==0 | n==0:
        return 0
    row_paths = [1 for _ in range(n)]
    for row in range(m-1):
        new_row_paths = [1]
        for col in range(1,n):
            new_row_paths.append(new_row_paths[-1]+row_paths[col])
        
        row_paths=new_row_paths

    return row_paths[-1]

print(uniquePaths(3,7))