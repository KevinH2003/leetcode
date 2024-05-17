from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = SortedDict()
        out = []
        
        for i in range(k - 1):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        for i in range(len(nums) - k + 1):
            j = i + k - 1
            
            left = nums[i]
            right = nums[j]
            
            counts[right] = counts.get(right, 0) + 1
            
            out.append(counts.peekitem()[0])
            
            counts[left] -= 1
            
            if counts[left] == 0:
                counts.pop(left)
            
        return out
            
            
        