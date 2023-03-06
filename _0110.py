# Definition for a binary tree node.
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


if __name__ == "__main__":
    print("===================0000===================")
    root = TreeNode()
    root.val = 3
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # obj = Solution()
    # test = obj.twoSum(root)
    # print (test)
