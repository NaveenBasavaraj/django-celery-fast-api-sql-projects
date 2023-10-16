def reverse_recursive(head):
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverse_recursive(head.next)
        head.next.next = head
    head.next = None
    return newHead


def reverse_iterative(head):
    prev, curr = None, head
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
        