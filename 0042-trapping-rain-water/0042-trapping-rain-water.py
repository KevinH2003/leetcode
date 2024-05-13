class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        
        leftgoing = 0
        rightgoing = 0
        
        for i in range(n):
            j = n - i - 1
            
            max_left[i] = leftgoing
            max_right[j] = rightgoing
            
            leftgoing = max(height[i], leftgoing)
            rightgoing = max(height[j], rightgoing)
            
        out = 0
        
        for i in range(n):
            out += max(0, min(max_left[i], max_right[i]) - height[i])
            
        return out