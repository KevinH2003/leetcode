class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        longest = 0
        visited = set()
        
        while right < len(s):
            curr = s[right]
            if curr in visited:
                longest = max(right - left, longest)
                
                while curr in visited:
                    visited.remove(s[left])
                    left += 1
            
            visited.add(curr)
            right += 1
            
        longest = max(right - left, longest)
            
        return longest
                