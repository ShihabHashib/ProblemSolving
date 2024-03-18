import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 145. Binary Tree Postorder Traversal


def postorderTraversal(root):
    result = []

    def postOrder(root):
        if not root:
            return

        postOrder(root.left)
        postOrder(root.right)
        result.append(root.val)

    postOrder(root)
    return result


# END
