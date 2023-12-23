import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2678. Number of Senior Citizens


def countSeniors(details):
    count = 0
    for i in details:
        if int(i[11:13]) > 60:
            count += 1

    return count


# END

details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
result = countSeniors(details)
display(result)
