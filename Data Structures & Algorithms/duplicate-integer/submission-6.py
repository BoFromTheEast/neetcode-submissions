class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numContainer = set()

        for i in nums:
            if i not in numContainer:
                numContainer.add(i)
            else:
                return True

        return False