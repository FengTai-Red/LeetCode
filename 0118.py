# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1], [1, 1]]
        if numRows < 3:
            return [[1]] if numRows == 1 else result
        else:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                result.append([1])
                for j in range(0, i-1):
                    result[i].append(((result[i-1][j]) + (result[i-1][j+1])))
                result[i].append(1)
        return result


if __name__ == "__main__":
    print("===================0000===================")
    print(Solution().generate(20))
