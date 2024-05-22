import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 100. Same Tree


def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# END
p = [1,2,3]
q = [1,2,3]
result = isSameTree(p, q)
display(result)
