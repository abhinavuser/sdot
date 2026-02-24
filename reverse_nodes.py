# 25. Reverse Nodes in k-Group
class Solution:
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev, cur = end, start
            while cur != end:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            start = group_prev.next
            group_prev.next = reverse(start, group_next)
            group_prev = start
