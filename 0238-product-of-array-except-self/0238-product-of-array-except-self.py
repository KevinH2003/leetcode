class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        leftgoing = 1
        for i in range(len(nums) - 1):
            num = nums[i]
            
            leftgoing *= num
            left[i + 1] = leftgoing
        
        rightgoing = 1
        for i in range(len(nums) - 1, 0, -1):
            num = nums[i]
            
            rightgoing *= num
            right[i - 1] = rightgoing
            
        for i in range(len(nums)):
            out[i] = left[i] * right[i]
            
        return out