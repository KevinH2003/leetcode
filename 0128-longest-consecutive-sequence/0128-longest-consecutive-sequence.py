class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        longest = 0
        
        for num in nums:
            if (num - 1) in numset:
                continue
            
            curr = num
            while curr in numset:
                curr += 1
            
            sequence_length = curr - num
            
            longest = max(longest, sequence_length)
            
        return longest