class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        charIndices = []
        for i in range(len(s)):
            if s[i] == c:
                charIndices.append(i)
                
        ret = []
        curr = 0
        for i in range(len(s)):
            if i > charIndices[curr] and curr < (len(charIndices) - 1):
                curr+= 1

            if (curr > 0):
                ret.append(min(abs(i - charIndices[curr]), abs(i - charIndices[curr - 1])))
            else:
                ret.append(abs(i - charIndices[curr]))
                
        return ret