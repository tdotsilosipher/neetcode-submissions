class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # set up count dict
        # create list of lists of freq[i], where freq[i] will store the number that appear i times
        count = {}
        # len 3 = 0, 1, 2, so + 1, range is exclusive, so 4 = 0 , 1, 2
        freq = [[] for i in range(len(nums) + 1)]

        # count how many each num appears
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        #range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
