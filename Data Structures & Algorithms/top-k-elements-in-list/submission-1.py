class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count how many of each number exists
        count = {}

        freq = [[] for i in range(len(nums)+1)]

        # make an array and put the number in the amount it has in the array
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        #loop through array till u find the kth number
        ans = []
        #range start stop step
        for i in range(len(freq)-1, 0 , -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
