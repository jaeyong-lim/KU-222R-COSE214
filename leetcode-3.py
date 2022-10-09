# Leetcode assignment #3
# 169. Majority Element
# Submitted 5 Oct 2022

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count, size = 0, 0, len(nums)
        for i in range(size):
            if count == 0:
                num = nums[i]
            if num == nums[i]:
                count += 1
            else:
                count -= 1
        return num
