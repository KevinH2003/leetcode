class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1 for i in range(n)]
        
        leftgoing = 1
        rightgoing = 1
        
        for i in range(n):
            j = n - i - 1
            
            out[i] *= leftgoing
            out[j] *= rightgoing
            
            leftgoing *= nums[i]
            rightgoing *= nums[j]
            
        return out
            
            
            