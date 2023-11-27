import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1282. Group the People Given the Group Size They Belong To


def groupThePeople(groupSizes):
    result = []
    groups = {}

    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []

        groups[size].append(i)

        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result


# END
groupSizes = [3, 3, 3, 3, 3, 1, 3]

result = groupThePeople(groupSizes)
display(result)
