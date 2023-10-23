import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 83. Remove Duplicates from Sorted List


def deleteDuplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

# END
