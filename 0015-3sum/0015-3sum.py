class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        out = []
        
        prev = None
        for i, target in enumerate(nums):
            if target > 0:
                break
            if target == prev:
                continue
                
            left = i + 1
            right = n
            
            while left < right:
                summed = target + nums[left] + nums[right]
                
                if summed > 0:
                    right -= 1
                elif summed < 0:
                    left += 1
                else:
                    out.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
            prev = target
            
        return out
            