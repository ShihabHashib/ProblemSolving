import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 144. Binary Tree Preorder Traversal


def inorderTraversal(root):
    result = []

    def preOrder(root):
        if not root:
            return

        result.append(root.val)
        preOrder(root.left)
        preOrder(root.right)

    preOrder(root)
    return result


# END
