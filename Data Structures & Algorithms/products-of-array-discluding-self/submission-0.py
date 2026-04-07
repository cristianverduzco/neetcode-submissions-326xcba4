class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums) 
        # left pass
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        # right pass
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output