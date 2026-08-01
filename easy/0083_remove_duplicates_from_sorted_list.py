from typing import Optional
from wsgiref.validate import header_re


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def create_linked_list(nums):
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


solution = Solution()

head = create_linked_list([1,1,2])
result = solution.deleteDuplicates(head)
print_linked_list(result)

head = create_linked_list([1,1,2,3,3])
result = solution.deleteDuplicates(head)
print_linked_list(result)