class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        longest = 0
        
        visited = set()
        while right < len(s):
            if s[right] in visited:
                longest = max(right - left, longest)
                
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left += 1
            
            visited.add(s[right])
            right += 1
            
        longest = max(right - left, longest)
            
        return longest
                