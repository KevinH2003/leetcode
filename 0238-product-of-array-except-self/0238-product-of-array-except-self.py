class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n # 24 12 8 6
        
        leftgoing = 1 # 6
        rightgoing = 1 # 24
        for i in range(0, n):
            j = n - i - 1
            
            out[i] *= leftgoing
            out[j] *= rightgoing
            
            leftgoing *= nums[i]
            rightgoing *= nums[j]
            
        return out