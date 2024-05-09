class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search(nums, target, left, right):
            if left >= right:
                return left if nums[left] == target else -1
            
            mid = (left + right) // 2
            
            mid_num = nums[mid]
            if mid_num > target:
                return b_search(nums, target, left, mid - 1)
            elif mid_num < target:
                return b_search(nums, target, mid + 1, right)
            else:
                return mid
            
        left = 0
        right = len(nums) - 1
        
        return b_search(nums, target, left, right)