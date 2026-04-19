class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstString = {}
        secondString = {}

        for str in s:
            firstString[str] = firstString.get(str,0) + 1

        for str in t:
            secondString[str] = secondString.get(str, 0) + 1

        return secondString == firstString