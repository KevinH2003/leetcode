class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0;
        while n:
            count += 1 if n % 2 else 0
            n = n >> 1
        return count