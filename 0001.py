# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    leng = len(nums)
    for i in range(leng):
        for j in range(i+1, leng):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
