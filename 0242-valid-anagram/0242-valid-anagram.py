class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        
        for c in s:
            if c not in smap:
                smap[c] = 1
            else:
                smap[c] += 1
        
        for c in t:
            if c not in tmap:
                tmap[c] = 1
            else:
                tmap[c] += 1
                
        for c in smap.keys():
            if c not in tmap.keys():
                return False
            if smap[c] != tmap[c]:
                return False
            
        for c in tmap.keys():
            if c not in smap.keys():
                return False
            
        return True