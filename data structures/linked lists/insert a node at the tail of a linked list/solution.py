def Insert(head, data):
    if not head:
        head = Node(data)
    else:
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = Node(data)
        
    return head