class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sortedNums = sorted(nums)

        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            left = i + 1
            right = len(sortedNums) - 1
            while left < right:
                if sortedNums[left] + sortedNums[right] + sortedNums[i] > 0:
                    right -= 1
                elif sortedNums[left] + sortedNums[right] + sortedNums[i] < 0:
                    left += 1
                else:
                    ans.append([sortedNums[i],sortedNums[left],sortedNums[right]])
                    left += 1 
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left-1]:
                        left += 1
                    continue
                    
        return ans
            