def CompareLists(headA, headB):
    while headA != None and headB != None and headA.data == headB.data:
        headA = headA.next
        headB = headB.next
    return 1 if headA == headB else 0