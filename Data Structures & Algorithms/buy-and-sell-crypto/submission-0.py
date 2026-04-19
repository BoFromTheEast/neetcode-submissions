class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[r]- prices[l])
            
            while prices[l] > prices[r]:
                l += 1
            r += 1
            if res < 0:
                res = 0
        return res


        