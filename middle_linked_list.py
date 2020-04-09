class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        start, end = head, head
        while end.next:
            start = start.next
            if end.next.next is None:
                end = end.next
            else:
                end = end.next.next
        return start

