import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 48. Rotate Image


def rotate(matrix):
    l = 0
    r = len(matrix) - 1

    while l < r: 
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)    
# END
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

result = rotate(matrix)
display(result)
