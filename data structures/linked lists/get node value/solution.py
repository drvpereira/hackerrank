def GetNode(head, position):
    stack = []
    while head:
        stack.append(head)
        head = head.next
    
    result = None
    while position >= 0:
        result = stack.pop()
        position -= 1

    return result.data