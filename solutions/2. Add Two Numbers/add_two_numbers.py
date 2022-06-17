# Definition for singly-linked list.

from curses.ascii import SO
from logging import root
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        root = node

        if not l1:
            return l2
        if not l2:
            return l1
        
        node.val += l1.val + l2.val
        carry = node.val // 10
        node.val = node.val % 10
        l1 = l1.next
        l2 = l2.next

        while l1 or l2 or carry > 0:
            node.next = ListNode(carry)
            node = node.next

            if l1:
                node.val += l1.val
                l1 = l1.next

            if l2:
                node.val += l2.val
                l2 = l2.next

            carry = node.val // 10
            node.val = node.val % 10

        return root



    def list2node_helper(self, l: List[int]) -> Optional[ListNode]:     
        n = len(l)   
        if n == 0: return None

        node = ListNode(l[0])
        root = node

        for i in range(1,n):
            node.next = ListNode(l[i])
            node = node.next
        
        return root


def print_helper(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()



if __name__ == "__main__":
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]
    l1 = [0]
    l2 = [0]

    s = Solution()
    listNode1 = s.list2node_helper(l1)
    listNode2 = s.list2node_helper(l2)

    node1 = listNode1
    print("list node 1: ")
    print_helper(node1)

    node2 = listNode2
    print("list node 2: ")
    print_helper(node2)

    node = s.addTwoNumbers(listNode1, listNode2)

    print("result: ")
    print_helper(node)


