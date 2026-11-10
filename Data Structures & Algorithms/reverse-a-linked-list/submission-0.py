# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None

        # at the end prev needs to be the new head
        while ptr:
            ptrNext = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = ptrNext
        return prev

