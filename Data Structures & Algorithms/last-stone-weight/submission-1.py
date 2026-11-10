class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # n * nlogn, space comp of n/1

        #brute force, sort everytime, pop two biggest and add to stones if not 0 until 1 left
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
            