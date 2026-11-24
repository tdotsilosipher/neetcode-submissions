class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get count of each number
        # put number in arr[count]
        # iterate backwards from count array and get top k

        #.items() key, value
        # enumrate idx, value
        freq = [[] for i in range(len(nums) +  1)]
            


        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for key, amount in count.items():
            freq[amount].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

            
