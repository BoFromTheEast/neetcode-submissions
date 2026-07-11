class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        matchs = {}
        matcht = {}

        for i in s:
            matchs[i] = matchs.get(i,0) + 1
        
        for i in t:
            matcht[i] = matcht.get(i,0) + 1
        
        return True if matchs == matcht else False