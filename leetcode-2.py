# Leetcode assignment #2
# 88. Merge Sorted Array
# Submitted 26 Sep 2022

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        i, j, k = m-1, n-1, m+n-1
        
        while k >= 0:
            if i < 0 or nums1[i] <= nums2[j] and j >= 0:
                nums1[k] = nums2[j]
                j -= 1

            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1
