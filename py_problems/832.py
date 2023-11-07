import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 832. Flipping an Image


def flipAndInvertImage(image):
    result = []
    for img in image:
        result.append([1 - x for x in reversed(img)])
    return result


# END
image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

result = flipAndInvertImage(image)
display(result)
