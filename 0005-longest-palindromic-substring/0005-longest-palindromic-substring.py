class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = set([""])
        
        for length in range(len(s)):
            for i in range(len(s) - length):
                j = i + length
                
                if s[i:j + 1] in palindromes:
                    continue
                
                if i == j:
                    palindromes.add(s[i])
                        
                if s[i] == s[j]:
                    if s[i + 1: j] in palindromes:
                        palindromes.add(s[i: j + 1])
                        
        return max(palindromes, key=lambda x: len(x))
                
                
        