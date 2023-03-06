# 88. 合并两个有序数组
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m = m - 1
        n = n - 1
        sum_mn = m + n + 1
        while(m >= 0 and n >= 0):
            if(nums1[m] >= nums2[n]):
                nums1[sum_mn] = nums1[m]
                m -= 1
            else:
                nums1[sum_mn] = nums2[n]
                n -= 1
            sum_mn -= 1
        if (m <= 0):
            for i in range(n + 1):
                nums1[i] = nums2[i]
        else:
            for i in range(m + 1):
                nums1[i] = nums1[i]
        return nums1


if __name__ == "__main__":
        nums1 = [0,0,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        test = Solution().merge(nums1, m, nums2, n)
        print(test)
