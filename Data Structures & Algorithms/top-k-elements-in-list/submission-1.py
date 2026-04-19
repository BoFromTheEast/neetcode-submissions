class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1) ]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for i, j in freq.items():
            count[j].append(i)

        res = []

        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                if len(res) == k:
                    break
                res.append(n)
                

        return res