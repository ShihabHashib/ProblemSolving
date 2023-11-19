import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2807. Insert Greatest Common Divisors in Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertGreatestCommonDivisors(head):
    current = head

    def greatestCoDiv(a, b):
        while b:
            a, b = b, a % b
        return a

    while current and current.next:
        gcd_value = greatestCoDiv(current.val, current.next.val)
        new_node = ListNode(gcd_value)
        new_node.next = current.next
        current.next = new_node
        current = current.next.next

    return head

# END


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Creating linked list [18,6,10,3]
head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
print("Original linked list::")
print_linked_list(head)

# Insert GCD nodes
new_head = insertGreatestCommonDivisors(head)
print("\nBellow is the result for::")
print_linked_list(new_head)
