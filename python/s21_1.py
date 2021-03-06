from structure import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pp = None
        res = None
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            if p1 is None and p2 is not None:
                p = p2
                p2 = p2.next
            elif p1 is not None and p2 is None:
                p = p1
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    p = p1
                    p1 = p1.next
                else:
                    p = p2
                    p2 = p2.next
            if pp is not None:
                pp.next = p
                pp = pp.next
            else:
                pp = res = p
        return res


l1 = ListNode.fromList([1, 2, 4])
l2 = ListNode.fromList([1, 3, 4])
lm=Solution().mergeTwoLists(l1, l2)
print(lm)
