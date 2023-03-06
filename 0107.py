# 107. 二叉树的层次遍历 II
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if (root == None):
            return []
        queue = [root]
        lis = []
        while(queue):
            li = [] 
            for l in range(len(queue)):
                node = queue.pop(0)
                li.append(node.val)
                if (node.left != None):
                    queue.append(node.left)
                if (node.right != None):
                    queue.append(node.right)
            lis.append(li)
        return lis[::-1]

if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    print(Solution().levelOrderBottom(a))