class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for str in strs:
            char_appearances = [0] * 26
            
            for c in str:
                char_appearances[ord(c) - ord("a")] += 1
            
            anagrams.setdefault(tuple(char_appearances), []).append(str)
            
        return list(anagrams.values())