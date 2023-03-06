# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1], [1, 1], [1, 2, 1]]
        if rowIndex < 3:
            return [1] if rowIndex == 0 else result[rowIndex]
        else:
            result = [[1], [1, 1]]
            for i in range(2, rowIndex +1 ):
                result.append([1])
                for j in range(0, i-1):
                    result[i].append(((result[i-1][j]) + (result[i-1][j+1])))
                result[i].append(1)
        return result[-1]

if __name__ == "__main__":
    print("===================0000===================")
    print(Solution().getRow(3))
