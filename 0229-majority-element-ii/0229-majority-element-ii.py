class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {} 
        res = set()
        
        for num in nums: 
            if num in freq: 
                freq[num] += 1
            else: 
                freq[num] = 1
            if freq[num] > len(nums) // 3 and num not in res: 
                res.add(num)
        
        return list(res)
        