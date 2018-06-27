"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1 > 3 > 1 > 1 > 1 minimizes the sum.
"""

import sys
class Solution(object):
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(cols-1, -1, -1):
            dp[rows-1][i] = grid[rows-1][i] + dp[rows-1][i+1]
        for j in range(rows-1, -1, -1):
            dp[j][cols-1] = grid[j][cols-1] + dp[j+1][cols-1]
        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        return dp[0][0]

    def minPathSum_dfs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = [sys.maxint]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, tmp_sum):
            if r == rows - 1 and c == cols - 1:
                if res[0] > tmp_sum:
                    res[0] = tmp_sum
                return
            if r < rows - 1 and tmp_sum+grid[r+1][c] < res[0]:
                dfs(r+1, c, tmp_sum+grid[r+1][c])
            if c < cols - 1 and tmp_sum+grid[r][c+1] < res[0]:
                dfs(r, c+1, tmp_sum+grid[r][c+1])
        dfs(0, 0, grid[0][0])
        return res[0]


grid = \
    [[1,1,8,1],
     [1,5,1,2],
     [3,2,1,4],
     [1,1,1,2]]
print Solution().minPathSum(grid)
