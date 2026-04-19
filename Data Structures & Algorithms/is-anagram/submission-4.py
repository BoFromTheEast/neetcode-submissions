class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = {}
        counter2 = {}

        for val in s:
            if val not in counter1:
                counter1[val] = counter1.get(val, 0) + 1
            else:
                counter1[val] += 1

        for char in t:
            if char not in counter2:
                counter2[char] = counter2.get(char, 0) + 1
            else:
                counter2[char] += 1

        return True if counter1 == counter2 else False
