class Solution:
    def twoSum(self, nums, target):
        storage = {}
        for i, num in enumerate(nums):
            need = target - num 
            if need in storage: 
                return [storage[need], i]
            storage[num] = i
        return []