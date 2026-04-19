class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrlen = len(nums)

        prefix = [1] * arrlen
        postfix = [1] * arrlen
        prefix[0] = nums[0]
        postfix[arrlen-1] = nums[arrlen-1]

        for i in range(1,arrlen):
            prefix[i] = prefix[i-1] * nums[i] 

        for i in range(arrlen-2, 0, -1):
            postfix[i] = postfix[i+1] * nums[i]

        ans = [1] * arrlen
        ans[0] = postfix[1]
        for i in range(1,arrlen):
            if i == arrlen-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1]*postfix[i+1]
        
        return ans