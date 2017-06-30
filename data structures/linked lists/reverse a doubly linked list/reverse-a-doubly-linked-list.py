def Reverse(head):
    while head:
        current, head = head, head.next        
        current.prev, current.next = current.next, current.prev
    return current