class KthLargest:
# Intuition:
# insert then sort everytime then return 
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[-(self.k)]
