class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        max = 0
        
        for num in nums:
            if (num - 1) in numset:
                continue
            
            sequence_length = 0
            curr = num
            while curr in numset:
                sequence_length += 1
                curr += 1
                
            if sequence_length > max:
                max = sequence_length
            
        return max