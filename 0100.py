# 100. 相同的树
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 示例 1:
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# 输出: true
# 示例 2:
# 输入:      1          1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# 输出: false
# 示例 3:
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# 输出: false

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q == None):
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    c1 = TreeNode(3)
    b1 = TreeNode(2)
    a1 = TreeNode(1, b1, c1)

    c2 = TreeNode(3)
    b2 = TreeNode(2)
    a2 = TreeNode(1, b2, c2)
    print(Solution().isSameTree(a1, a2))
