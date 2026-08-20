class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    pA = headA
    pB = headB
    while pA != pB:
        if pA is None:
            pA = headB
        else:
            pA = pA.next
        if pB is None:
            pB = headA
        else:
            pB = pB.next
    return pA


# Example 1
# A: 4 -> 1 \
#              8 -> 4 -> 5
# B: 5 -> 6 -> 1 /

common1 = ListNode(8)
common1.next = ListNode(4)
common1.next.next = ListNode(5)

headA1 = ListNode(4)
headA1.next = ListNode(1)
headA1.next.next = common1

headB1 = ListNode(5)
headB1.next = ListNode(6)
headB1.next.next = ListNode(1)
headB1.next.next.next = common1

result1 = getIntersectionNode(headA1, headB1)

if result1:
    print("Example 1: Intersected at", result1.val)
else:
    print("Example 1: No intersection")


# Example 2
# A: 1 -> 9 -> 1 \
#                   2 -> 4
# B:           3  /

common2 = ListNode(2)
common2.next = ListNode(4)

headA2 = ListNode(1)
headA2.next = ListNode(9)
headA2.next.next = ListNode(1)
headA2.next.next.next = common2

headB2 = ListNode(3)
headB2.next = common2

result2 = getIntersectionNode(headA2, headB2)

if result2:
    print("Example 2: Intersected at", result2.val)
else:
    print("Example 2: No intersection")


# Example 3
# A: 2 -> 6 -> 4
#
# B: 1 -> 5

headA3 = ListNode(2)
headA3.next = ListNode(6)
headA3.next.next = ListNode(4)

headB3 = ListNode(1)
headB3.next = ListNode(5)

result3 = getIntersectionNode(headA3, headB3)

if result3:
    print("Example 3: Intersected at", result3.val)
else:
    print("Example 3: No intersection")