import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        minHeap = []

        for num in nums:
            mapper[num] = mapper.get(num,0) + 1

        for num, freq in mapper.items():
            heapq.heappush(minHeap, [freq,num])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []    
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
