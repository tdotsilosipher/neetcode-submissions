class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        #dfs use on one side and not use on another
        # index, current combination (list), total
        def dfs(i, cur, total):
            # 2 stop cases
            # if hit
            if total == target:
                res.append(cur.copy())
                return
            # if limits
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            # with
            dfs(i, cur, total + nums[i])
            # remove previous to reuse
            cur.pop()
            # does not include
            dfs(i+1, cur, total)


        dfs(0, [], 0 )
        return res