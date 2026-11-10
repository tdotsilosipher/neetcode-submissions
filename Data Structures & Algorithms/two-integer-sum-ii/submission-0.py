class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use hashmap dict to store numbers: index
        # and check if complement exists in hashmap already
        seen = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[numbers[i]] = i