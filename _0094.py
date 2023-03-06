# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, item):
        # 创建一个新节点
        node = TreeNode(item)
        # 队列的方式实现，队列最开始存根
        queue = [node]
        # 循环处理队列
        while queue:
            # 从头取，第一次取的是根节点
            cur = queue.pop(0)
            print(cur.left)
            # 判断取出的节点有没有左值或右值，左节点为空，则添加新节点
            if cur.left is None:
                cur.left = node
                return
            else:
                # 左节点不是空，则将左节点添加队列
                queue.append(cur.left)
            if cur.right is None:
                cur.right == node
                return
            else:
                queue.append(cur.right)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


if __name__ == "__main__":
    print("===================0000===================")
#            5
#           / \
#      11         17        
#     / \         / \
#    n   n      3    10
#             /  \
#           6      5
#          / \    / \
#         1   2  4   3
    # root2 = TreeNode()
    # root2.val = 5
    # root2.left = TreeNode(11)
    # root2.right = TreeNode(17, 
    # TreeNode(3,
    #     TreeNode(6, TreeNode(1), TreeNode(2)),
    #     TreeNode(5, TreeNode(4), TreeNode(3))), 
    # TreeNode(10))
    # print(Solution().inorderTraversal())
    root = TreeNode(1)
    for i in range (0, 20):
        root.add(i)

