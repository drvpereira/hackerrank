def Reverse(head):
    rev_list = []
    while head:
        rev_list.append(head)
        head = head.next
        
    if len(rev_list) > 0:
        head = rev_list.pop()
        tail = head
        while len(rev_list) > 0:
            tail.next = rev_list.pop()
            tail = tail.next
        tail.next = None
        return head
    else:
        return None