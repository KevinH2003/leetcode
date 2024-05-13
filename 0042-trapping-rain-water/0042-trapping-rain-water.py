class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        maxleft, maxright = 0, 0
        
        left = 0
        right = n - 1
            
        out = 0
        
        while left <= right:
            if maxleft < maxright:
                heightleft = height[left]
                out += max(0, maxleft - heightleft)
                
                if maxleft < heightleft:
                    maxleft = heightleft
                    
                left += 1
            else:
                heightright = height[right]
                out += max(0, maxright - height[right])
                
                if maxright < height[right]:
                    maxright = height[right]
                    
                right -= 1
            
        return out