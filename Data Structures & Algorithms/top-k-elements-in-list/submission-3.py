from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)


        top_keys = heapq.nlargest(k, freq.keys(), key=freq.get)

        return top_keys