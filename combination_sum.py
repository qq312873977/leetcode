"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(nums, tgt, tmp_res, sumof):
            for i in nums:
                if sumof + i == tgt:
                    tmp = tmp_res+[i]
                    tmp.sort()
                    if tmp not in res:
                        res.append(tmp)
                    return
                elif sumof + i < tgt:
                    dfs(nums, tgt, tmp_res+[i], sumof+i)
                else:
                    break
        dfs(candidates, target, [], 0)
        return res


print Solution().combinationSum([1,2,3,4,5,7], 7)