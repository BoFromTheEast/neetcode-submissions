class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sContainer = {}
        tContainer = {}

        for i in s:
            sContainer[i] = sContainer.get(i,0) + 1
        for j in t:
            tContainer[j] = tContainer.get(j,0) + 1

        return sContainer == tContainer