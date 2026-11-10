class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep track of opening, if closing pair check if top is valid pair and then pop
        # use dict to keep pairs
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in pairs:
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        