class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        find = {}

        for i, j in enumerate(nums):
            seen = target - j
            if seen in find:
                return [find[seen], i]
            else:
                find[j] = i
        