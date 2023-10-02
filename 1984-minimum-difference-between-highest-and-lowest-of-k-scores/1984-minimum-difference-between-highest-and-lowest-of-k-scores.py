class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = k - 1
        min = nums[j] - nums[i]
        
        while j < len(nums):
            diff = nums[j] - nums[i]
            if diff < min:
                min = diff
            i += 1
            j += 1
            
        return min