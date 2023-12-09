import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2951. Find the Peaks


def findPeaks(mountain):
    result = []
    for i in range(1, len(mountain) - 1):
        print(i)
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            result.append(i)

    return result


# END
mountain = [1, 4, 3, 8, 5]

result = findPeaks(mountain)
display(result)
