# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMiddle(head):
            prev = None
            slow = fast = head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None
            
            return slow
        
        if not head:
            return None
        
        mid = findMiddle(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
