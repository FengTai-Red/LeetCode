# 83. 删除排序链表中的重复元素
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 示例 1:
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
# 输入: 1->1->2->3->3
# 输出: 1->2->3

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = head
        if (x == None):
            return None
        while(head != None):
            if(head.next == None):
                break
            temp = head.val
            if(temp == head.next.val):
                head.next = head.next.next
            else:
                head = head.next
        return x
        
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(2)
    e = ListNode(2)
    f = ListNode(2)
    g = ListNode(2)
    h = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    Solution().deleteDuplicates(a)
    while(a != None):
        print(a.val)
        a = a.next