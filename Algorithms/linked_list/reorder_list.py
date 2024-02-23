def reorder_list(head):
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    
    second = slow.next
    prev = slow.next = None # cut the list
    
    while second:
        temp = second.next # keep track of next node
        second.next = prev
        prev = second
        second = temp
    
    # merge the two halfs
    first, second = head, prev
    
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2