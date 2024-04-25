import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 231. Power of Two

import math

def isPowerOfTwo(n):
    if n < 0 :
        return False
    if bin(n).count('1') == 1:
        return True
    return False


    # num = math.log10(n) / math.log10(2)
    # return math.ceil(num) == math.floor(num)


# END
n = 0

result = isPowerOfTwo(n)
display(result)
