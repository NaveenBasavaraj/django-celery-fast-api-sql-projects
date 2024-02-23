from linked_list import ListNode

## Merge two sorted lists

def mergeTwoSortedLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

## Merge k sorted lists

def mergeKsortedLists(list_nodes):
    if not list_nodes or len(list_nodes) == 0:
        return None
    
    while len(list_nodes) > 1:
        mergeLists = []
        for i in range(0, len(list_nodes), 2):
            l1 = list_nodes[i]
            l2 = list_nodes[i+1] if (i+1) < len(list_nodes) else None
            mergeLists.append(mergeKsortedLists(l1, l2))
        lists = mergeLists
    return lists[0]