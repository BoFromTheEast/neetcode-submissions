class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = {}
        counter2 = {}

        for val in s:
            counter1[val] = counter1.get(val, 0) + 1

        for char in t:
            counter2[char] = counter2.get(char, 0) + 1


        return True if counter1 == counter2 else False
