class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        
        for c in s:
            smap[c] = smap.setdefault(c, 0) + 1
        
        for c in t:
            tmap[c] = tmap.setdefault(c, 0) + 1
        
        if smap.keys() != tmap.keys():
            return False
        
        for c in smap.keys():
            if smap[c] != tmap[c]:
                return False
            
        return True