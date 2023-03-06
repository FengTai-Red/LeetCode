# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    height = len(nums)
    if (target > nums[-1]):
        return height
    if (target < nums[0]):
        return 0
    while (low < height):
        mid = (low + height) // 2
        if (target > nums[mid]):
            low = mid + 1
        elif (target < nums[mid]):
            height = mid
        else:
            return mid
    return low

if __name__ == "__main__":
    nums1 = [1,3,5,6] # 2
    target1 = 5
    nums2 = [1,3,5,6] # 1
    target2 = 2
    nums3 = [1,3,5,6] # 4
    target3 = 7
    nums4 = [1,3,5,6] # 0
    target4 = 0
    nums5 = [1,3] # 1
    target5 = 2
    print(searchInsert(nums2, target2))
