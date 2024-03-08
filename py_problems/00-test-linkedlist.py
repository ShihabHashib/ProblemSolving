import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 00. Test LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)

    def dis_LinkedList(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next

    # Code start Here ==================

    def count(self):
        count = 0
        cur = self.head

        while cur:
            count += 1
            cur = cur.next

        return count

    def find_mid(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val


# Create linked list from array
arr = [4, 5, 6, 7, 15, 31, 55, 12, 2, 54, 3]
ll = LinkedList()
for num in arr:
    ll.append(num)

# Display original linked list
print("Given Linked List:")
ll.dis_LinkedList()


print(ll.find_mid())
