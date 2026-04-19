class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
        ex = set()

        for i in nums:
            if i in ex:
                return True
            ex.add(i)
        return False
