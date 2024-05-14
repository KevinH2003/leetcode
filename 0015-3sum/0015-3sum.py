class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        nums.sort()
        
        for i in range(len(nums)):
            target = nums[i]
            if target == nums[i - 1] and i != 0:
                continue
            if target > 0:
                break
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                summed = target + nums[left] + nums[right]
                if summed == 0:
                    out.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
                elif summed > 0:
                    right -= 1
                else:
                    left += 1
            
        return out
                