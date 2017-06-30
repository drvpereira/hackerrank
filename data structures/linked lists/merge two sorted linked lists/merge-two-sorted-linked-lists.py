
def MergeLists(head_a, head_b):
    new_head, new_tail = None, None
    
    if (head_a and head_b and head_a.data < head_b.data) or (head_a and not head_b):
        new_head, new_tail = head_a, head_a
        head_a = head_a.next
    else:
        new_head, new_tail = head_b, head_b
        head_b = head_b.next

    while head_a and head_b:
        if head_a.data < head_b.data:
            new_tail.next = head_a
            head_a = head_a.next
        else:
            new_tail.next = head_b
            head_b = head_b.next
        new_tail = new_tail.next
        
    while head_a:
        new_tail.next = head_a
        new_tail = new_tail.next
        head_a = head_a.next

    while head_b:
        new_tail.next = head_b
        new_tail = new_tail.next
        head_b = head_b.next
        
    return new_head