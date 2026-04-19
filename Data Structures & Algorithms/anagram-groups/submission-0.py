from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        listofWords = defaultdict(list)
        for chars in strs:
            sortedKey = "".join(sorted(chars))
            listofWords[sortedKey].append(chars) 
        
        return list(listofWords.values())