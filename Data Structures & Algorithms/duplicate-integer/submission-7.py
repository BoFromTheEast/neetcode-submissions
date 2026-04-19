class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set()

        for val in nums:
            if val not in counter:
                counter.add(val)
            else:
                return True
            
        return False