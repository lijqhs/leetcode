## [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

```python
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
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
