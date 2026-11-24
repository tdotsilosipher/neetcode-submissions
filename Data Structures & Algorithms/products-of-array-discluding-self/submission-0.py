class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force would just be calculate each at O(n^2)

        res = [1] * (len(nums))

        # 1 2 3 4
        # 1 1 2 6
        # 24 12 8 6

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res