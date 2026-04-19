class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordCountA = {}
        wordCountB = {}
        
        for i in s:
            if i not in wordCountA:
                wordCountA[i] = wordCountA.get(i,0) + 1
            wordCountA[i] = wordCountA[i] + 1
        
        for j in t:
            if j not in wordCountB:
                wordCountB[j] = wordCountB.get(j,0) + 1
            wordCountB[j] = wordCountB[j] + 1

        return True if wordCountA == wordCountB else False    
        

        