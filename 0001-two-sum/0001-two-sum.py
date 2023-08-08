class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberDictionary = {}
        for i in range(len(nums)):
            numberDictionary[target - nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in numberDictionary and j != numberDictionary[nums[j]]:
                return [numberDictionary[nums[j]], j]
        #hiiiiiiiii
                
        
        
