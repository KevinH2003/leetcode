class Solution:
    def climbStairs(self, n: int) -> int:
        # base case (n = 0 => 1, n = 1 => 1)
        # final case
        # order of iteration (order of inductive step) n++
        # data structure
        # recurrence relation (inductive step proof)
        
        # given you have climbStairs(0) ... climbStairs(k), find climbStairs(k + 1)
        # climbStairs(k) = climbStairs(k - 1) + climbStairs(k - 2)
        
        ways_to_climb = [0] * max(2, (n + 1))
        ways_to_climb[0] = 1
        ways_to_climb[1] = 1
        
        for i in range(2, n + 1):
            ways_to_climb[i] = ways_to_climb[i - 1] + ways_to_climb[i - 2]
            
        return ways_to_climb[n]
        
        
        