// Leetcode assignment #1
// 35. Search Insert Position
// Submitted 14 Sep 2022

int searchInsert(int* nums, int numsSize, int target)
{
    // Base case
    if (numsSize == 0)
        return 0;
    
    int mid = numsSize / 2;
    int compare = nums[mid] - target;
    
    if (compare > 0)
    {
        // Search left half
        return searchInsert(nums, mid, target);
    }
    else if (compare < 0)
    {
        // Search right half
        return mid + 1 + searchInsert(nums + mid + 1, numsSize - (mid + 1), target);
    }
    else
    {
        return mid;
    }
}
