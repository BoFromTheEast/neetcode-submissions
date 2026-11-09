class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumFind = {}

        for i in range(len(nums)):

            find = target - nums[i]
            
            if find not in sumFind:
                sumFind[nums[i]] = i
            else:
                return [sumFind[find],i]
        