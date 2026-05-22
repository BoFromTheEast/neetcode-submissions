class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for idx, num in enumerate(nums):
            findingNum = target - num
            if findingNum not in mapper:
                mapper[num] = idx
            else:
                return [mapper[findingNum],idx]
        