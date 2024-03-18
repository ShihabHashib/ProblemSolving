import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 94. Binary Tree Inorder Traversal


def inorderTraversal(root):
    result = []

    def inOrder(root):
        if not root:
            return

        inOrder(root.left)
        result.append(root.val)
        inOrder(root.right)

    inOrder(root)
    return result


# END
