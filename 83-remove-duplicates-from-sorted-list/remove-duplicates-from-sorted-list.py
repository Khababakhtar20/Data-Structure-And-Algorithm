# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current:
            # skip all nodes that have the same value
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            # move forward
            current = current.next
        return head
