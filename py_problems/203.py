import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 203. Remove Linked List Elements


def removeElements(head, val):
    while head is not None and head.val == val:
        head = head.next

    temp = head

    while temp is not None and temp.next is not None:
        if temp.next.val == val:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head

# END
