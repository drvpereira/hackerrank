def RemoveDuplicates(head):
    current, previous = head, None
    
    while current:
        if previous and current.data == previous.data:
            previous.next = current.next
        else:
            previous = current
        current = current.next
    
    return head