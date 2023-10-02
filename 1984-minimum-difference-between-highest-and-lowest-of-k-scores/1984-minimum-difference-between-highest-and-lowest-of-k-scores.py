class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, k - 1
        minimum = float("inf")
        
        while j < len(nums):
            minimum = min(minimum, nums[j] - nums[i])
            i += 1
            j += 1
            
        return minimum