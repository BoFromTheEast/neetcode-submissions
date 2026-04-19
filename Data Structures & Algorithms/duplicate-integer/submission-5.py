class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = set()

        for i in nums:
            if i not in container:
                container.add(i)
            else:
                return True
        return False