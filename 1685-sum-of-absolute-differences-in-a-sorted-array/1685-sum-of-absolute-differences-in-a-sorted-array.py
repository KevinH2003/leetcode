class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Given a list of integers `nums`, this function computes an array where each element
        is the sum of absolute differences between the corresponding element in `nums` and all other elements.
        """
        
        n = len(nums)
        ret = []
        
        left_sum = 0
        right_sum = sum(nums)
        
        # Iterate through each element of nums
        for i, num in enumerate(nums):
            right_sum -= num
            
            left_len = i
            right_len = n - i - 1
            
            # Calculate the sum of absolute differences for the current element
            ret.append((left_len * num - left_sum) + (right_sum - right_len * num))
            
            left_sum += num
        
        return ret
        