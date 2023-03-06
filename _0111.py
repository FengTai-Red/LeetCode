# Definition for a binary tree node.
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.flag = True

        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1:
                self.flag = False
            return max(l, r) + 1

        height(root)
        return self.flag

if __name__ == "__main__":
    print("===================0000===================")
    #    3
    #  9   20
    # n n 15 7
    root = TreeNode()
    root.val = 3
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

#             5
#      11             17        
#    n    n       3           10
#              6     5
#             1 2   4 3
    root2 = TreeNode()
    root2.val = 5
    root2.left = TreeNode(11)
    root2.right = TreeNode(17, 
    TreeNode(3,
        TreeNode(6, TreeNode(1), TreeNode(2)),
        TreeNode(5, TreeNode(4), TreeNode(3))), 
    TreeNode(10))

    print(Solution().isBalanced(root2))