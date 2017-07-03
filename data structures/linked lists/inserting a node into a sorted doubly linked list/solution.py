def SortedInsert(head, data):
    tail = head
    while tail.next and tail.next.data < data:
        tail = tail.next
    
    new_node = Node(data, tail.next, tail)
    if tail.next:
        tail.next.prev = new_node
    tail.next = new_node
    
    return head