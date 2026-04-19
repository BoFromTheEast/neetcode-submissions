class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       sums = {}

       for i, n in enumerate(nums):
            val = target - n
            if val in sums:
                return [sums[val],i]
            sums[n] = i
