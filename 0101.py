# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 进阶：
# 你可以运用递归和迭代两种方法解决这个问题吗？
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def a(node1, node2):
            if (node1 == None and node2 == None):
                return True
            if (node1 == None or node2 == None):
                return False
            if (node1.val != node2.val):
                return False
            return a(node1.left, node2.right) and a(node1.right, node2.left)
        return a(root, root)
    

if __name__ == "__main__":

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(None)
    e = TreeNode(3)
    f = TreeNode(None)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

#        a
#        1
#     b     c
#     2     2
#    d e   f g
#    N 3   N 3
    print(Solution().isSymmetric(a))
