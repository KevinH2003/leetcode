class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        max = 0
        
        for num in nums:
            if (num - 1) in numset:
                continue
            
            curr = num
            while curr in numset:
                curr += 1
            
            sequence_length = curr - num
            
            if sequence_length > max:
                max = sequence_length
            
        return max