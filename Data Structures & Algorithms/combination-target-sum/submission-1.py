class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # i is cur index, cur is current combination, total is sum of numbers
        def dfs(i, cur, total):
            # if u found target already
            if total == target:
                res.append(cur.copy())
                return
                
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            # include and add to toal
            dfs(i, cur, total + nums[i])
            cur.pop()
            # not include
            dfs(i +1, cur, total)

        dfs(0, [], 0)
        return res