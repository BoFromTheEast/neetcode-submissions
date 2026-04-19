class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSets = set()

        for num in nums:
            if num in numSets:
                return True
            else:
                numSets.add(num)
        
        return False