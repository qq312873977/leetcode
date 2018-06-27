"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(left, right, s):
            if left < n:
                dfs(left+1, right, s+'(')
            if right == n:
                res.append(s)
                return
            else:
                if left > right:
                    dfs(left, right+1, s+')')
        dfs(0, 0, '')
        return res

print Solution().generateParenthesis(4)