def Delete(head, position):
    current_position = 0
    prev_node = None
    curr_node = head
        
    while current_position < position:
        current_position += 1
        prev_node = curr_node
        curr_node = curr_node.next

    if prev_node and curr_node:
        prev_node.next = curr_node.next
    elif prev_node:
        prev_node.next = None
    else:
        head = curr_node.next
            
    return head
  
