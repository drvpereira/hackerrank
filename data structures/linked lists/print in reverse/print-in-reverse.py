def ReversePrint(head):
    reversed = []
    while head:
        reversed.append(head)
        head = head.next
    while reversed:
        print(reversed.pop().data)
        