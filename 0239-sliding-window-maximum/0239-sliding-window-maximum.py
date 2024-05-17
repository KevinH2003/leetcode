from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        out = []
        
        for i in range(0, k - 1):
            while len(q) > 0 and nums[i] > q[-1]:
                q.pop()
            
            q.append(nums[i])
            
        for i in range(len(nums) - k + 1):
            j = i + k - 1
            
            left = nums[i]
            right = nums[j]
            
            while len(q) > 0 and right > q[-1]:
                q.pop()
                
            q.append(right)
            out.append(q[0])
            
            if left == q[0]:
                q.popleft()
            
        return out
            
            
        