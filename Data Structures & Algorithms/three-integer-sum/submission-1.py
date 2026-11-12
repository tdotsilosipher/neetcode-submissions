class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        end = len(nums)
        ans = []
        nums.sort()
        #range is not inclusive
        for i in range(end - 2):
            # if first number is not negative no possible answer
            if nums[i] > 0:
                break
            # check duplicates after first
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, end - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
        return ans