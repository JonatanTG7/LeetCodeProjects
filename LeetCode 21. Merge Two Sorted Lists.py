# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        d = ListNode()
        current = d

        while list1 is not None and list2 is not None:
            if (list1.val == list2.val):
                current.next = list1
                current = list1
                list1 = list1.next
                current.next = list2
                current = list2
                list2 = list2.next

            elif (list1.val < list2.val):
                current.next = list1
                current = list1
                list1 = list1.next

            elif (list1.val > list2.val):
                current.next = list2
                current = list2
                list2 = list2.next

        while list1 is not None:
            current.next = list1
            current = list1
            list1 = list1.next

        while list2 is not None:
            current.next = list2
            current = list2
            list2 = list2.next

        return linked_list_to_list(d.next)

# From linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# From list to linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
result = solution.mergeTwoLists(list_to_linked_list(list1),list_to_linked_list(list2))
print(result)


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]