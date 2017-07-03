def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        prev_node = head
        next_node = head.next
        
        current_position = 1
        while current_position < position:
            prev_node = next_node
            next_node = next_node.next
            current_position += 1
        prev_node.next = Node(data, next_node)
        return head