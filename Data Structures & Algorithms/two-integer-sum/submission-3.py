class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, n in enumerate(nums):
            want = target - n
            if want in result:
                return [result[want],i]
            else:
                result[n] = i