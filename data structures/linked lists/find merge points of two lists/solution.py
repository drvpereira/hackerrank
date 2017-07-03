def FindMergeNode(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next or headB
        b = b.next or headA
    return a.data