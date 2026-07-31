class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = set(nums)
        seq = 0

        for i in nums:
            if(i-1) not in count:
                length = 0
                while(i+length) in count:
                    length += 1
                seq = max(length, seq)
            

        return seq