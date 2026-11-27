class Solution:

# approach from fixed prefix (0 : idx - 1) and free suffix: (idx to end)
# n! * n
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        #back track from 0
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):
        # if we have full permutation add to solution
        if idx == len(nums):
            self.res.append(nums[:])
            return

        for i in range(idx, len(nums)):
            # swap idx with i
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            # original (backtrack)
            nums[idx], nums[i] = nums[i], nums[idx]