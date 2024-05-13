class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        nums.sort()
        
        prev = None
        for i in range(n):
            target = - nums[i]
            
            if target == prev:
                continue
            if target < 0:
                break
            
            summands = {}
            visited = set()
            
            for j in range(i + 1, n):
                if nums[j] in summands.keys() and nums[j] not in visited:
                    out.append([nums[i], summands[nums[j]], nums[j]])
                    visited.add(nums[j])
                    visited.add(summands[nums[j]])
                    
                summands[target - nums[j]] = nums[j]
            
            prev = target
            
        return out