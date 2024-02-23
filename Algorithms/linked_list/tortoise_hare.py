# linked list cycle
# tortoise and hare algorithm
# floyds cycle detection



def has_floyd_cycle(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False