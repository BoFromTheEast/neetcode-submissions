class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counter = {}

        for i, j in enumerate(nums):
            find = target - j
            if find in counter:
                return [counter[find],i]
            counter[j] = i

            