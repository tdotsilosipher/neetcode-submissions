class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        #nlogn sort

        #n * 2^n

        # copying is O(n)
        # dfs is 2^n
        # dfs time is significant more than nlogn
        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for i in range(idx, len(candidates)):
                # if not starting number and duplicate
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                # if adding would make it bigger than target
                if total + candidates[i] > target:
                    break
                #choose
                cur.append(candidates[i])
                #explore
                dfs(i + 1, cur, total + candidates[i])
                #undo
                cur.pop()
        
        dfs(0, [], 0)

        return res