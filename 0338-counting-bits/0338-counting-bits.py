class Solution:
    def countBits(self, n: int) -> List[int]:
    
        ret = [0]
        msb = 0
        for i in range(1, n + 1):
            if (i >= msb):
                msb = 1 if msb == 0 else msb * 2
            ret.append(1 + ret[i - msb])
            
        return ret
            