def has_cycle(head):
    p1 = head.next
    p2 = head
    
    while p2:
        while p1:
            if p1 == p2:
                return True
            p1 = p1.next
        p2 = p2.next

    return False