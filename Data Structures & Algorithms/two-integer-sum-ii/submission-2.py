class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        ans = 0
        
        while left < right:
            ans = numbers[left] + numbers[right]
            
            if ans == target:
                return [left +1 , right + 1]
            if ans > target:
                right -= 1
                continue
            if ans < target:
                left += 1
                continue
        