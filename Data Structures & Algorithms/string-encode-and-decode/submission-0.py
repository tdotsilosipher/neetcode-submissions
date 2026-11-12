class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string get length then do length#string and append to result
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append("#")
            ans.append(i)
            #join with no spaces
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        return ans