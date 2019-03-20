'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 快慢指针(一刷)
        first = ListNode(0)    # 处理长度为一，删除后，为空链表的请款，需要设置一个虚节点
        first.next = head
        fast,slow = first,first
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return first.next


        # Approach one  双指针，前后距离为n  （二刷）
        first = second = head
        while n:
            first = first.next
            n -= 1
        if not first : return head.next
        while first.next:     # 前指针定位到最后一个结点，后指针位于要删除结点的前面一位
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
