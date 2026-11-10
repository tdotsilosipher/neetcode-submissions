class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # time: O(n * 2^n)
        # each number is included and not included (2) and there are N numbers = 2^n (number of subsets)
        # each subset could be length N so N * 2^n

        def dfs(i):
            # stop case
            if i >= len(nums):
                res.append(subset.copy())
                return
            # includes nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # does not include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res