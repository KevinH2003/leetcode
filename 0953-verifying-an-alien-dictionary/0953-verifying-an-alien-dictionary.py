class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def strcmp(word1, word2, dict):

            for p in range(min(len(word1), len(word2))):
                if word1[p] != word2[p]:
                    return dict[word1[p]] < dict[word2[p]]
                
            return len(word1) <= len(word2)
        
        dict = {}
        for i in range(len(order)):
            dict[order[i]] = i
        
        for i in range(len(words) - 1):
            if not strcmp(words[i], words[i + 1], dict):
                return False
            
        return True