class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        maxleft = 0
        maxright = 0
        
        left = 0
        right = n - 1
            
        out = 0
        
        while left <= right:
            if maxleft < maxright:
                out += max(0, maxleft - height[left])
                if maxleft < height[left]:
                    maxleft = height[left]
                left += 1
            else:
                out += max(0, maxright - height[right])
                if maxright < height[right]:
                    maxright = height[right]
                right -= 1
            
        return out