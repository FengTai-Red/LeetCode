# 69.x 的平方根
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 示例 1:
# 输入: 4
# 输出: 2
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        height = x
        while(True):
            mid = (low + height) // 2
            a = mid * mid
            b = (mid + 1) * (mid + 1)
            if (a <= x and x < b):
                return mid
            elif (b > x):
                height = mid - 1
            else:
                low = mid + 1

if __name__ == "__main__":
    print(Solution().mySqrt(4))