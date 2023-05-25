class Solution:
    def countBits(self, n: int) -> List[int]:
    
        ret = []
        for i in range(n + 1):
            num1s = 0;
            while i:
                i = i & (i - 1)
                num1s += 1
            ret.append(num1s)
        return ret
            