class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        def recurse(left, right):
            if left >= right:
                return nums[right]
            
            mid = (left + right) // 2
            
            if nums[mid] >= nums[left] and nums[mid] >= nums[right]:
                return recurse(mid + 1, right)
            else:
                return recurse(left, mid)
            
        return recurse(left, right)
            
            