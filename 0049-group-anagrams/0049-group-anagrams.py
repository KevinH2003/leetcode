class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        dic = {}
        for s in strs:
            key=1
            for c in s:
                key*=vals[ord(c)-ord('a')]
            if key not in dic:
                dic[key] = []
            dic[key].append(s)
        res=[]
        for key,val in dic.items():
            res.append(val)
        return res