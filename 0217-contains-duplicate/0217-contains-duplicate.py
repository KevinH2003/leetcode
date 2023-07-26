class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        
        for i in dict.values():
            if (i > 1):
                return True
            
        return False
        