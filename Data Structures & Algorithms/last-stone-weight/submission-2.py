class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heap

        # min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        #pop top 2
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
        # second is greater than first x-y
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])