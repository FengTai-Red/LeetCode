# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: ListNode
    :type list2: ListNode
    :rtype: ListNode
    """
    if (list1 == None):
        return list2
    if (list2 == None):
        return list1
    if (list1.val <= list2.val):
        l3 = list1
        list1 = list1.next
    else:
        l3 = list2
        list2 = list2.next
    t = l3
    while(list1 != None and list2 != None):
        if (list1.val < list2.val):
            t.next = list1
            t = t.next
            list1 = list1.next
        else:
            t.next = list2
            t = t.next
            list2 = list2.next
    if (list1 == None):
        t.next = list2
    if (list2 == None):
        t.next = list1
    return l3

if __name__ == "__main__":
    list1_a = ListNode(7)
    list1_b = ListNode(5, list1_a)
    list1_c = ListNode(1, list1_b)

    list2_a = ListNode(11)
    list2_b = ListNode(3, list2_a)
    list2_c = ListNode(1, list2_b)

    l3 = mergeTwoLists(list1_c, list2_b)
    while(l3 != None):
        print(l3.val)
        l3 = l3.next
