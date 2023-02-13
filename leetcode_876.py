# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=algorithm-i

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
